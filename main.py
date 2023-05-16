from random import *

class Maze:
    """
    Classe Labyrinthe
    Représentation sous forme de graphe non-orienté
    dont chaque sommet est une cellule (un tuple (l,c))
    et dont la structure est représentée par un dictionnaire
      - clés : sommets
      - valeurs : ensemble des sommets voisins accessibles
    """

    def __init__(self, height, width, empty):
        """
        Constructeur d'un labyrinthe de height cellules de haut
        et de width cellules de large
        Les voisinages sont initialisés à des ensembles vides
        Remarque : dans le labyrinthe créé, chaque cellule est complètement emmurée
        """
        self.height = height
        self.width = width
        self.empty = empty

        self.neighbors = {(i, j): set() for i in range(height) for j in range(width)}

        if empty:
            for i in range(self.height):
                for j in range(self.width):
                    # case en-dessous
                    if i + 1 < self.height:
                        self.neighbors[(i, j)].add((i + 1, j))
                        self.neighbors[(i + 1, j)].add((i, j))

                    # case au-dessus
                    if i - 1 > self.height:
                        self.neighbors[(i, j)].add((i - 1, j))
                        self.neighbors[(i - 1, j)].add((i, j))

                    # case droite
                    if j + 1 < self.width:
                        self.neighbors[(i, j)].add((i, j + 1))
                        self.neighbors[(i, j + 1)].add((i, j))

                    # case gauche
                    if j - 1 > self.width:
                        self.neighbors[(i, j)].add((i, j - 1))
                        self.neighbors[(i, j - 1)].add((i, j))

    def info(self):
        """
        **NE PAS MODIFIER CETTE MÉTHODE**
        Affichage des attributs d'un objet 'Maze' (fonction utile pour deboguer)
        Retour:
            chaîne (string): description textuelle des attributs de l'objet
        """
        txt = "**Informations sur le labyrinthe**\n"
        txt += f"- Dimensions de la grille : {self.height} x {self.width}\n"
        txt += "- Voisinages :\n"
        txt += str(self.neighbors)+"\n"
        valid = True
        for c1 in {(i, j) for i in range(self.height) for j in range(self.width)}:
            for c2 in self.neighbors[c1]:
                if c1 not in self.neighbors[c2]:
                    valid = False
                    break
            else:
                continue
            break
        txt += "- Structure cohérente\n" if valid else f"- Structure incohérente : {c1} X {c2}\n"
        return txt

    def __str__(self):
        """
        **NE PAS MODIFIER CETTE MÉTHODE**
        Représentation textuelle d'un objet Maze (en utilisant des caractères ascii)
        Retour:
             chaîne (str) : chaîne de caractères représentant le labyrinthe
        """
        txt = ""
        # Première ligne
        txt += "┏"
        for j in range(self.width-1):
            txt += "━━━┳"
        txt += "━━━┓\n"
        txt += "┃"
        for j in range(self.width-1):
            txt += "   ┃" if (0,j+1) not in self.neighbors[(0,j)] else "    "
        txt += "   ┃\n"
        # Lignes normales
        for i in range(self.height-1):
            txt += "┣"
            for j in range(self.width-1):
                txt += "━━━╋" if (i+1,j) not in self.neighbors[(i,j)] else "   ╋"
            txt += "━━━┫\n" if (i+1,self.width-1) not in self.neighbors[(i,self.width-1)] else "   ┫\n"
            txt += "┃"
            for j in range(self.width):
                txt += "   ┃" if (i+1,j+1) not in self.neighbors[(i+1,j)] else "    "
            txt += "\n"
        # Bas du tableau
        txt += "┗"
        for i in range(self.width-1):
            txt += "━━━┻"
        txt += "━━━┛\n"

        return txt

    def add_wall(self, c1, c2):
        """
        Ajoute un mur du labyrinthe entre c1 et c2
        on retire tout simplement c2 dans les voisins de c1 et c1 dans les voisins de c2
        """
        # Facultatif : on teste si les sommets sont bien dans le labyrinthe
        assert 0 <= c1[0] < self.height and \
               0 <= c1[1] < self.width and \
               0 <= c2[0] < self.height and \
               0 <= c2[1] < self.width, \
            f"Erreur lors de l'ajout d'un mur entre {c1} et {c2} : les coordonnées de sont pas compatibles avec les dimensions du labyrinthe"
        # Ajout du mur
        if c2 in self.neighbors[c1]:  # Si c2 est dans les voisins de c1
            self.neighbors[c1].remove(c2)  # on le retire
        if c1 in self.neighbors[c2]:  # Si c3 est dans les voisins de c2
            self.neighbors[c2].remove(c1)  # on le retire

    def remove_wall(self, c1, c2):
        """
        Retire le mur du labyrinthe entre c1 et c2
        on ajoute tout simplement c2 dans les voisins de c1 et c1 dans les voisins de c2
        """
        # Facultatif : on teste si les sommets sont bien dans le labyrinthe
        assert 0 <= c1[0] < self.height and \
               0 <= c1[1] < self.width and \
               0 <= c2[0] < self.height and \
               0 <= c2[1] < self.width, \
            f"Erreur lors de la suppression d'un mur entre {c1} et {c2} : les coordonnées de sont pas compatibles avec les dimensions du labyrinthe"
        # Suppression du mur
        if c2 not in self.neighbors[c1]:  # Si c2 n'est dans les voisins de c1
            self.neighbors[c1].add(c2)  # on l'ajoute
        if c1 not in self.neighbors[c2]:  # Si c1 n'est dans les voisins de c2
            self.neighbors[c2].add(c1)  # on l'ajoute

    def get_walls(self):
        """
        Accesseur aux murs du labyrinthe
        return : list de tous les murs, les murs sous sont formes de tuple (c1,c2)
        """
        lstWalls = []
        for i in range(self.height):
            for j in range(self.width):
                # case en-dessous
                if i + 1 < self.height and (i, j) not in self.neighbors[(i + 1, j)] and (i + 1, j) not in \
                        self.neighbors[(i, j)]:
                    lstWalls = lstWalls + [[(i, j), (i + 1, j)]]

                # case au-dessus
                if i - 1 > self.height and (i, j) not in self.neighbors[(i - 1, j)] and (i - 1, j) not in \
                        self.neighbors[(i, j)]:
                    lstWalls = lstWalls + [[(i, j), (i - 1, j)]]

                # case droite
                if j + 1 < self.width and (i, j) not in self.neighbors[(i, j + 1)] and (i, j + 1) not in self.neighbors[
                    (i, j)]:
                    lstWalls = lstWalls + [[(i, j), (i, j + 1)]]

                # case gauche
                if j - 1 > self.width and (i, j) not in self.neighbors[(i, j - 1)] and (i, j - 1) not in self.neighbors[
                    (i, j)]:
                    lstWalls = lstWalls + [[(i, j), (i, j - 1)]]

        return lstWalls

    def fill(self):
        """
        Permet de rendre un labyrinthe rempli de murs
        on vide tout les voisins de toutes les cellules
        """
        for i in range(self.height):
            for j in range(self.width):
                self.neighbors[i, j].clear()

    def emptyFunction(self):
        """
        Permet de rendre un labyrinthe sans aucun mur, on parcours toutes les cellules
        et on test si elle a des voisins, si oui on retire le wall entre cette cellule et la cellule voisine
        """
        for i in range(self.height):
            for j in range(self.width):

                #case au-dessous
                if i + 1 < self.height:
                    self.remove_wall((i,j),(i+1,j))

                # case au-dessus
                if i - 1 > self.height:
                    self.remove_wall((i, j),(i-1, j))

                # case droite
                if j + 1 < self.width:
                    self.remove_wall((i, j),(i, j+1))

                # case gauche
                if j - 1 > self.width:
                    self.remove_wall((i, j),(i, j-1))


    def get_contiguous_cells(self,c):
        """
        Accesseur aux "voisins" de la celulle c, c'est-à-dire les celulles qui peuvent potentiellement être atteinte si il n'y a pas de mur
        return : list des cellules atteignable (mur ou non) de la cellule passée en parametre
        """

        lstContiguousCells = []

        #case en dessous
        if c[0] + 1 < self.height:
            lstContiguousCells = lstContiguousCells + [(c[0] + 1,c[1])]

        # case au-dessus
        if c[0] - 1 < self.height and c[0]-1 >= 0:
            lstContiguousCells = lstContiguousCells + [(c[0] - 1,c[1])]

        # case droite
        if c[1] + 1 < self.width:
            lstContiguousCells = lstContiguousCells + [(c[0],c[1]+1)]

        # case gauche
        if c[1] - 1 < self.width and c[1]-1 >= 0 :
            lstContiguousCells = lstContiguousCells + [(c[0],c[1]-1)]

        return lstContiguousCells


    def get_reachable_cells(self,c):
        """
        Accesseur aux "voisins" de la celulle c qui sont atteignable
        return : list des cellules atteignable (il n'y a pas de mur) de la cellule passée en parametre
        """

        #je recupere la liste des murs du laby + la liste des cellules potentiellement atteignable depuis la cell c
        lstWalls = self.get_walls()
        lstContiguousCells = self.get_contiguous_cells(c)
        ind = []
        
        #parcours de toutes les cellules potentiellement atteignable depuis la cell c
        for i in range(len(lstContiguousCells)):
            cell1 = [c,lstContiguousCells[i]]
            cell2 = [lstContiguousCells[i], c]
            for j in range(len(lstWalls)):
                
                #si cell1 ou cell2 est dans lstWalls cela veut dire qu'il y a un mur et par conséquent qu'elle n'est pas atteignable
                #je sauvegarde donc l'indice de la celulle non atteignable
                if cell1 == lstWalls[j] or cell2 == lstWalls[j]:
                    ind = ind + [i]

        #j'inverse l'orde comme ça je commence par la fin
        ind = sorted(ind,reverse=True)

        #je parcours la liste des indices et je supprime ces cellules dans ma liste des cellules potentiellement atteignable depuis la cell c
        #en effet je réutilise cette liste pour m'éviter d'en recréer une
        for k in range(len(ind)):
            del lstContiguousCells[ind[k]]

        return lstContiguousCells

    @classmethod
    def gen_btree(cls,h,w):
        """
        Permet de générer un labyrinthe grâce à l'algorithme de btree
        return : le laby généré
        """
        laby = Maze(h,w,empty=False)
        for i in range(h):
            for j in range(w):
                lstCoordCellule = []

                #mur sud
                if i+1 < h :
                    lstCoordCellule = lstCoordCellule + [(i+1,j)]

                #mur est
                if j+1 < w:
                    lstCoordCellule = lstCoordCellule + [(i,j+1)]

                #si jai un mur sud et un mur est ou un des deux
                if len(lstCoordCellule) > 0 :
                    if len(lstCoordCellule) == 2 :
                        temp = randint(0, 1)
                        laby.remove_wall((i,j),lstCoordCellule[temp])

                    else:
                        laby.remove_wall((i,j),lstCoordCellule[0])

        return laby

    @classmethod
    def gen_sidewinder(cls, h, w):
        """
        Permet de générer un labyrinthe grâce à l'algorithme de sidewinder
        return : le laby généré
        """
        laby = Maze(h, w, empty=False)
        for i in range(h - 1):
            sequence = []
            for j in range(w - 1):

                #j'ajoute ma cellule a une sequence
                sequence = sequence + [(i, j)]

                #choix aleatoire : si 0 je casse le mur EST
                temp = randint(0, 1)
                if temp == 0:
                    laby.remove_wall((i, j), (i, j + 1))

                #si c'est 1 je casse le mur SUD d'une cell au hasard dans ma liste de sequence et je réinitialise la liste sequence
                else:
                    temp = randint(0, len(sequence) - 1)
                    laby.remove_wall(sequence[temp], (sequence[temp][0] + 1, sequence[temp][1]))
                    sequence = []

            #j'ajoute la derniere cellule et je retire au hasard une cell pour detruire son mur SUD
            sequence = sequence + [(i, w - 1)]
            temp = randint(0, len(sequence) - 1)
            laby.remove_wall(sequence[temp], (sequence[temp][0] + 1, sequence[temp][1]))

        #je casse tous les murs EST de la derniere ligne du laby
        for k in range(w - 1):
            laby.remove_wall((h - 1, k), (h - 1, k + 1))

        return laby

    @classmethod
    def gen_fusion(cls,h, w):
        """
        Permet de générer un labyrinthe grâce à l'algorithme de fusion de chemins
        return : le laby généré
        """
        laby = Maze(h, w, empty=False)

        #j'initialise un dictionnaire de label, ou chaque cellule aura un label different
        label = {(i, j): 1 for i in range(h) for j in range(w)}
        labelNb = 0

        #j'attribue ici le label distinct pour chaque cellule
        for i in range(h):
            for k in range(w):
                label[(i, k)] = labelNb
                labelNb = labelNb + 1

        #tri aleatoire de la liste des murs du laby
        lstWalls = sample(laby.get_walls(), len(laby.get_walls()))

        #je parcours tous mes murs
        for j in range(len(lstWalls)):

            #si les deux cells n'ont pas le meme label, je casse le mur + j'affecte le label de ma premiere cellule à toutes les cellules
            #ayant le meme label que la deuxieme cellule
            if label[lstWalls[j][0]] != label[lstWalls[j][1]]:
                laby.remove_wall(lstWalls[j][0], lstWalls[j][1])
                temp = label[lstWalls[j][1]]
                label[lstWalls[j][1]] = label[lstWalls[j][0]]

                #petite boucle pour affecte le label de ma premiere cellule à toutes les cellules ayant le meme label que la deuxieme cellule 
                for p in range(h):
                    for m in range(w):
                        if label[(p, m)] == temp:
                            label[(p, m)] = label[lstWalls[j][0]]

        return laby

    @classmethod
    def gen_exploration(cls,h, w):
        """
        Permet de générer un labyrinthe grâce à l'algorithme de exploration exhaustive
        return : le laby généré
        """
        lstCell = []
        for i in range(h):
            for j in range(w):
                lstCell = lstCell + [(i, j)]

        randomcellule = lstCell[randint(0, len(lstCell) - 1)]
        laby = Maze(h, w, empty=False)
        Pile = [randomcellule]
        Visite = [randomcellule]
        temp = len(Pile)

        while temp > 0:
            cellActuel = Pile[0]
            del Pile[0]
            test = laby.get_contiguous_cells(cellActuel)

            cellCOntiVisit = True
            lstContigueNonVisite = []
            for i in range(len(test)):
                if test[i] not in Visite:
                    cellCOntiVisit = False
                    lstContigueNonVisite = lstContigueNonVisite + [test[i]]

            if cellCOntiVisit == False:
                Pile = Pile + [cellActuel]
                hasard = lstContigueNonVisite[randint(0, len(lstContigueNonVisite) - 1)]

                if cellActuel != hasard:
                    laby.remove_wall(cellActuel, hasard)
                    Visite = Visite + [hasard]
                    Pile = [hasard] + Pile

            temp = len(Pile)

        return laby

    @classmethod
    def gen_wilson(cls,h,w):
        """
        Permet de générer un labyrinthe grâce à l'algorithme de Wilson
        return : le laby généré
        """
        marque = []
        lstCellule = []
        for i in range(h):
            for j in range(w):
                lstCellule = lstCellule+ [(i, j)]
        laby = Maze(h, w, empty=False)
        randCell = lstCellule[randint(0,len(lstCellule)-1)]
        marque = marque + [randCell]

        while len(marque) != h*w:

            trouver = False

            while trouver == False:
                cellDepart = lstCellule[randint(0,len(lstCellule)-1)]
                if cellDepart not in marque:
                    trouver = True


            chemin = []
            chemin = chemin+[cellDepart]
            lstVoisins = laby.get_contiguous_cells(cellDepart)
            continuer = True


            while continuer == True:
                #je prends ma coord aleatoirement dans la liste des voisins, j'aurai 3 choses à vérifier
                cell = lstVoisins[randint(0,len(lstVoisins)-1)]

                # 1) si la cellule a deja ete parcourus dans le chemin actuelle -> je suis dans une boucle je dois donc
                #recommencer à zero -> je reinitalise mes variables à celle du début
                if cell in chemin:
                    chemin = []
                    chemin = chemin + [cellDepart]
                    lstVoisins = laby.get_contiguous_cells(cellDepart)

                # 2) sinon j'ajoute cette cellule à mon chemin et je prends ses cellules voisines
                else:
                    chemin = chemin + [cell]
                    lstVoisins = laby.get_contiguous_cells(cell)
                # 3) si la cellule est deja marque je stop ma boucle while pour casser tous les murs du chemin que
                #j'ai parcourus et ajouter toutes les cellules du chemin à la liste marque
                    if cell in marque:
                        continuer = False


            #je vais commencer par les marquer
            for i in range(len(chemin)):
                if chemin[i] not in marque:
                    marque = marque + [chemin[i]]


            #et je casse tous les murs
            for j in range(len(chemin)-1):

                laby.remove_wall(chemin[j],chemin[j+1])



        return laby
    
    def overlay(self, content=None):
        """
        Rendu en mode texte, sur la sortie standard, \
        d'un labyrinthe avec du contenu dans les cellules
        Argument:
            content (dict) : dictionnaire tq content[cell] contient le caractère à afficher au milieu de la cellule
        Retour:
            string
        """
        if content is None:
            content = {(i, j): ' ' for i in range(self.height) for j in range(self.width)}
        else:
            content = content | {(i, j): ' ' for i in range(
                self.height) for j in range(self.width) if (i, j) not in content}
        txt = r""
        # Première ligne
        txt += "┏"
        for j in range(self.width - 1):
            txt += "━━━┳"
        txt += "━━━┓\n"
        txt += "┃"
        for j in range(self.width - 1):
            txt += " " + content[(0, j)] + " ┃" if (0, j + 1) not in self.neighbors[(0, j)] else " " + content[
                (0, j)] + "  "
        txt += " " + content[(0, self.width - 1)] + " ┃\n"
        # Lignes normales
        for i in range(self.height - 1):
            txt += "┣"
            for j in range(self.width - 1):
                txt += "━━━╋" if (i + 1, j) not in self.neighbors[(i, j)] else "   ╋"
            txt += "━━━┫\n" if (i + 1, self.width - 1) not in self.neighbors[(i, self.width - 1)] else "   ┫\n"
            txt += "┃"
            for j in range(self.width):
                txt += " " + content[(i + 1, j)] + " ┃" if (i + 1, j + 1) not in self.neighbors[(i + 1, j)] else " " + content[(i + 1,j)] + "  "
            txt += "\n"
        # Bas du tableau
        txt += "┗"
        for i in range(self.width - 1):
            txt += "━━━┻"
        txt += "━━━┛\n"
        return txt

    def solve_dfs(self,D,A):
        """
        Permet de résoudre un labyrinthe par résolution en "profondeur", de la cell 'D' à la cell 'A'
        return : list des cellules à parcourir pour résoudre le laby dans l'odre
        """
        Pile = [D]
        pred = {}
        pred[D] = -1
        marque = []
        terminer = False

        while len(marque) < self.height*self.width and terminer == False:
            c = Pile[len(Pile)-1]
            del Pile[len(Pile)-1]

            if c == A:
                terminer = True

            else:
                lstVoisins = self.get_reachable_cells(c)
                for i in range(len(lstVoisins)):
                    if lstVoisins[i] not in marque:
                        marque = marque + [lstVoisins[i]]
                        Pile = Pile+[lstVoisins[i]]
                        pred[lstVoisins[i]] = c


        #reconstitution du chemin
        chemin = []
        temp = len(chemin)
        stop = False
        while len(pred)!=temp and stop == False :
            for i in range(len(pred)-1):
                if len(pred)!=temp and stop == False:
                    chemin = chemin+[c]
                    c = pred[c]
                    temp = len(chemin)
                    if c == D:
                        stop = True

        return chemin



    def solve_bfs(self, D, A):
        """
        Permet de résoudre un labyrinthe par résolution en "largeur", de la cell 'D' à la cell 'A'
        return : list des cellules à parcourir pour résoudre le laby dans l'odre
        """
        File = [D]
        marque = [D]
        pred = {}
        pred[D] = -1

        stop = False


        while len(File)>0 and stop == False:
            c = File[0]
            del File[0]
            if c == A:
                stop = True


            lstVoisins = self.get_reachable_cells(c)
            for i in range(len(lstVoisins)):
                if lstVoisins[i] not in marque:
                    File = File + [lstVoisins[i]]
                    marque = marque + [lstVoisins[i]]
                    pred[lstVoisins[i]] = c

        #reconstitution du chemin
        chemin = []
        while c != D:
            chemin = chemin+[c]
            c = pred[c]
        chemin = chemin+[D]


        return chemin

    def get_contiguous_cells2(self,c):
        """
        Fait exactement la meme chose que "get_contiguous_cells", cependant ici on prend les coords EST/SUD/OUEST/NORD dans ce sens de priorité
        car la resolution par main droite est comme un humain qu'on lacherait dans un laby -> il ira constamment a droite puis quand il est bloque SUD/OUEST/NORD
        """
        lstContiguousCells = []

        # case droite
        if c[1] + 1 < self.width:
            lstContiguousCells = lstContiguousCells + [(c[0], c[1] + 1)]

        #case en dessous
        if c[0] + 1 < self.height:
            lstContiguousCells = lstContiguousCells + [(c[0] + 1,c[1])]

        # case gauche
        if c[1] - 1 < self.width and c[1] - 1 >= 0:
            lstContiguousCells = lstContiguousCells + [(c[0], c[1] - 1)]


        # case au-dessus
        if c[0] - 1 < self.height and c[0]-1 >= 0:
            lstContiguousCells = lstContiguousCells + [(c[0] - 1,c[1])]



        return lstContiguousCells


    def get_reachable_cells2(self,c):
        """
        Fait exactement la meme chose que "get_reachable_cells", cependant ici on prend les coords EST/SUD/OUEST/NORD dans ce sens de priorité
        car la resolution par main droite est comme un humain qu'on lacherait dans un laby -> il ira constamment a droite puis quand il est bloque SUD/OUEST/NORD
        """
        lstWalls = self.get_walls()
        lstContiguousCells = self.get_contiguous_cells2(c)
        ind = []


        for i in range(len(lstContiguousCells)):
            temp = [c,lstContiguousCells[i]]
            temp2 = [lstContiguousCells[i], c]
            for j in range(len(lstWalls)):

                if temp == lstWalls[j] or temp2 == lstWalls[j]:
                    ind = ind + [i]

        ind = sorted(ind,reverse=True)

        for k in range(len(ind)):
            del lstContiguousCells[ind[k]]

        return lstContiguousCells

    def solve_rhr(self,D,A):
        """
        Permet de résoudre un labyrinthe par résolution par "main droite", de la cell 'D' à la cell 'A' 
        return : list des cellules à parcourir pour résoudre le laby dans l'odre
        """
        Pile = [D]
        pred = {}
        pred[D] = -1
        marque = []
        terminer = False

        while len(marque) < self.height*self.width and terminer == False:
            c = Pile[len(Pile)-1]
            del Pile[len(Pile)-1]

            if c == A:
                terminer = True

            else:
                lstVoisins = self.get_reachable_cells2(c)

                for i in range(len(lstVoisins)):
                    if lstVoisins[i] not in marque:
                        marque = marque + [lstVoisins[i]]
                        Pile = Pile+[lstVoisins[i]]
                        pred[lstVoisins[i]] = c


        #reconstitution du chemin
        chemin = []
        temp = len(chemin)
        stop = False
        while len(pred)!=temp and stop == False :
            for i in range(len(pred)-1):
                if len(pred)!=temp and stop == False:
                    chemin = chemin+[c]
                    c = pred[c]
                    temp = len(chemin)
                    if c == D:
                        stop = True

        return chemin
    

    def distance_geo(self,D,A):
        """
        Permet d'accéder à la distance geometrique d'un laby de la cell D à la cell A
        c'est à dire le nombre de case minimum qui separe les deux cellules
        return : int, distance géometrique entre la cell D à la cell A
        """
        chemin = self.solve_bfs(D, A)
        return len(chemin) - 2


    def distance_man(self,D,A):
        """
        Permet d'accéder à la distance de Manhattan d'un laby de la cell D à la cell A
        c'est à dire le nombre de case minimum qui separe les deux cellules si le labyrinthe n'aurait aucun mur
        return : int, distance Manhattan entre la cell D à la cell A
        """
        distance = 0
        if D[0] >= A[0]:
            distance = distance + (D[0]-A[0])
        else:
            distance = distance + (A[0] - D[0])

        if D[1] >= A[1]:
            distance = distance + (D[1]-A[1])
        else:
            distance = distance + (A[1] - D[1])

        return distance

    def comparer_algo(self):
        n = int(input("Combien de test voulez vous effectuer ? "))
        resultat = 0
        for i in range(n):
            laby = Maze.gen_exploration(15,15)
            resultat = resultat + round((laby.distance_geo((0,0),(14,14)))/(laby.distance_man((0,0),(14,14))),2)
        print("indicateur difficulté gen_exploration : ", round(resultat/n,3))

        resultat = 0
        for i in range(n):
            laby = Maze.gen_fusion(15, 15)
            resultat = resultat + round((laby.distance_geo((0, 0), (14, 14))) / (laby.distance_man((0, 0), (14, 14))),2)
        print("indicateur difficulté gen_fusion : ", round(resultat / n,3))

        resultat = 0
        for i in range(n):
            laby = Maze.gen_wilson(15, 15)
            resultat = resultat + round((laby.distance_geo((0, 0), (14, 14))) / (laby.distance_man((0, 0), (14, 14))),2)
        print("indicateur difficulté gen_wilson : ", round(resultat / n, 3))



        return