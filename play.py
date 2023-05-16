from pygame.examples import sound
from main import Maze
from random import *

import keyboard
import time
import os
import pygame
import colorama
import sys

# Fonction pour nettoyer le terminal
def clear_screen() :
    os.system('cls' if os.name == 'nt' else 'clear')

# Fonction pour vérifier les modules installés
def verifpaquets() :

    # verification du module time
    try:
        import time
        print('[MODULE] | import \033[32mOK\033[0m ')
    except ImportError:
        print('\033[32m[MODULE] | importer module << time >>\033[0m')

    time.sleep(0.5)

    # verification du module sys
    try:
        import sys
    except ImportError:
        print('\033[32m[MODULE] | importer module << sys >>\033[0m')
    else:
        print('[MODULE] | import \033[32mOK\033[0m ')

    time.sleep(0.5)

    # verification du module keyboard
    try:
        import keyboard
    except ImportError:
        print('\033[32m[MODULE] | importer module << keyboard >>\033[0m')
    else:
        print('[MODULE] | import \033[32mOK\033[0m ')

    time.sleep(0.5)

    # verification du module os
    try:
        import os
    except ImportError:
        print('\033[32m[MODULE] | importer module << os >>\033[0m')
    else:
        print('[MODULE] | import \033[32mOK\033[0m ')

    time.sleep(0.5)

    # verification du module pygame
    try:
        import pygame
    except ImportError:
        print('\033[32m[MODULE] | importer module << pygame >>\033[0m')
    else:
        print('[MODULE] | import \033[32mOK\033[0m ')

    time.sleep(0.5)

    # verification du module colorama
    try:
        import colorama
    except ImportError:
        print('\033[32m[MODULE] | importer module << colorama >>\033[0m')
    else:
        print('[MODULE] | import \033[32mOK\033[0m ')

    time.sleep(0.5)


def main_menu() :
    verifpaquets()
    if sys.version_info > (3, 9):
        print('[VERSION] | version \033[32mOK\033[0m ')
        time.sleep(1)

        # Initialiser modules
        pygame.init()
        colorama.init()
        pygame.mixer.init()

        # Charger la musique
        pygame.mixer.music.load("./music/music.wav")
        pygame.mixer.music.set_volume(0.2)


        # Jouer la musique en boucle
        pygame.mixer.music.play(loops=-1)

        # Nettoyer le terminal
        clear_screen()

        print("{:^124}".format( colorama.Fore.RED +"             __  __                 _____         _____       _   _                 "+ colorama.Style.RESET_ALL))
        print("{:^124}".format( colorama.Fore.GREEN +"     /\     |  \/  |               |_   _|       |  __ \     | | | |                "+ colorama.Style.RESET_ALL))
        print("{:^124}".format( colorama.Fore.YELLOW +"   /  \    | \  / | __ _ _______    | |  _ __   | |__) |   _| |_| |__   ___  _ __ "+ colorama.Style.RESET_ALL))
        print("{:^124}".format( colorama.Fore.BLUE +"   / /\ \   | |\/| |/ _` |_  / _ \   | | | '_ \  |  ___/ | | | __| '_ \ / _ \| '_ \ "+ colorama.Style.RESET_ALL))
        print("{:^124}".format( colorama.Fore.MAGENTA +"  / ____ \  | |  | | (_| |/ /  __/  _| |_| | | | | |   | |_| | |_| | | | (_) | | | |"+ colorama.Style.RESET_ALL))
        print("{:^124}".format( colorama.Fore.CYAN + " /_/    \_\ |_|  |_|\__,_/___\___| |_____|_| |_| |_|    \__, |\__|_| |_|\___/|_| |_|"+ colorama.Style.RESET_ALL))
        print("{:^124}".format( colorama.Fore.RED +"                                                         __/ |                      "+ colorama.Style.RESET_ALL))
        print("{:^124}".format( colorama.Fore.GREEN +"                                                        |___/                       "+ colorama.Style.RESET_ALL))
        print("{:^124}".format(""))
        entree = input("{:^124}".format(colorama.Fore.RED + "Appuyer sur 'Entrée' pour commencer | Entrer 'S' pour voir le tableau des scores " + colorama.Style.RESET_ALL))
        if entree == "s" :
            score = open("score.txt","r")
            print("\n")
            for ligne in score:
                print(ligne)
            ok = False
            print("\n\n")
            while ok == False:
                entree = input("Entrer 'Q' pour quitter l'affichage des scores ")
                if entree == "q":
                    ok = True

        return entree
    else:
        print('\033[32m[VERSION] | Veuillez installer la version 3.9 de python ou >\033[0m')

# Fonction d'écran de chargement
def loading() :
    def progress_bar(percent, length=20):
        # Symboles pour la barre de progression
        symbols = "█░"
        filled_length = int(length * percent)

        bar = symbols[0] * filled_length
        bar += symbols[1] * (length - filled_length)

        # Affichage barre de progression
        print(f"[{bar}] {percent * 100:.1f}%", end="\r")

    for i in range(101):
        progress_bar(i / 100)
        time.sleep(0.05)


def affiche_shuffle():
    print("{:^124}".format(
        colorama.Fore.RED + "  ____  _   _ _   _ _____ _____ _     _____ " + colorama.Style.RESET_ALL))
    print("{:^124}".format(
        colorama.Fore.GREEN + " / ___|| | | | | | |  ___|  ___| |   | ____|" + colorama.Style.RESET_ALL))
    print("{:^124}".format(
        colorama.Fore.YELLOW + " \___ \| |_| | | | | |_  | |_  | |   |  _|  " + colorama.Style.RESET_ALL))
    print("{:^124}".format(
        colorama.Fore.BLUE + "  ___) |  _  | |_| |  _| |  _| | |___| |___ " + colorama.Style.RESET_ALL))
    print("{:^124}".format(
        colorama.Fore.MAGENTA + " |____/|_| |_|\___/|_|   |_|   |_____|_____|" + colorama.Style.RESET_ALL))
    print("{:^124}".format(
        colorama.Fore.CYAN + "                                            " + colorama.Style.RESET_ALL))
    print("{:^124}".format(""))

def affiche_tp():
    print("{:^124}".format(
        colorama.Fore.RED + "  ____      _    _   _ ____   ___  __  __ " + colorama.Style.RESET_ALL))
    print("{:^124}".format(
        colorama.Fore.YELLOW + " |  _ \    / \  | \ | |  _ \ / _ \|  \/  |" + colorama.Style.RESET_ALL))
    print("{:^124}".format(
        colorama.Fore.BLUE + " | |_) |  / _ \ |  \| | | | | | | | |\/| |" + colorama.Style.RESET_ALL))
    print("{:^124}".format(
        colorama.Fore.RED + " |  _ <  / ___ \| |\  | |_| | |_| | |  | |" + colorama.Style.RESET_ALL))
    print("{:^124}".format(
        colorama.Fore.GREEN + " |_| \_\/_/   \_\_| \_|____/ \___/|_|  |_|" + colorama.Style.RESET_ALL))
    print("{:^124}".format(
        colorama.Fore.BLUE + "                                          " + colorama.Style.RESET_ALL))

def affiche_end():
    clear_screen()
    print("{:^124}".format(
        colorama.Fore.WHITE + "   ▄▄▄▄▀ ▄  █ ▄███▄       ▄███▄      ▄   ██▄   " + colorama.Style.RESET_ALL))
    print("{:^124}".format(
        colorama.Fore.WHITE + "▀▀▀ █   █   █ █▀   ▀      █▀   ▀      █  █  █  " + colorama.Style.RESET_ALL))
    print("{:^124}".format(
        colorama.Fore.WHITE + "    █   ██▀▀█ ██▄▄        ██▄▄    ██   █ █   █ " + colorama.Style.RESET_ALL))
    print("{:^124}".format(
        colorama.Fore.WHITE + "   █    █   █ █▄   ▄▀     █▄   ▄▀ █ █  █ █  █  " + colorama.Style.RESET_ALL))
    print("{:^124}".format(
        colorama.Fore.WHITE + "  ▀        █  ▀███▀       ▀███▀   █  █ █ ███▀  " + colorama.Style.RESET_ALL))
    print("{:^124}".format(
        colorama.Fore.WHITE + "          ▀                       █   ██       " + colorama.Style.RESET_ALL))


def affiche_help() :
    print("")
    print("Commandes d'aide")
    print("← : Q   ↑ : Z   → : D   ↓ : S")
    print("")
    print("Mute la musique : 'X' ")
    print("Reprendre la musique : 'C' ")
    print("Quitter : 'P' ")
    print("Recommencer : 'R' ")

def jouerSimple(h,w,persoStr : str,choixAlgo : int):
    #choix du labyrinthe aleatoire aleatoire si le joueur à mis 0 en param
    tempChoixAlgo = -1
    if choixAlgo == 0:
        tempChoixAlgo = 0
        choixAlgo = randint(1,3)

    #création du laby
    if choixAlgo == 1:
        laby = Maze.gen_exploration(h, w)
        print("Génération gen_exploration")

    elif choixAlgo == 2 :
        laby = Maze.gen_fusion(h, w)
        print("Génération gen_fusion")

    else:
        laby = Maze.gen_wilson(h, w)
        print("Génération gen_wilson")

    if tempChoixAlgo == 0:
        choixAlgo = 0


    affichageStuff = {}
    cell = (0, 0)
    cellFin = (h-1, w-1)
    affichageStuff[cell] = persoStr
    affichageStuff[cellFin] = colorama.Fore.CYAN + '░' + colorama.Style.RESET_ALL
    cellAlreadyUse = [cell]
    cellAlreadyUse = cellAlreadyUse + [cellFin]

    #generation aleatoire item qui nous fais spawn aleatoirement
    ok = False
    while ok == False:
        cellSpawn = (randint(0, laby.height - 1), randint(0, laby.width - 1))
        if cellSpawn not in cellAlreadyUse:
            affichageStuff[cellSpawn] = colorama.Fore.RED + 'o' + colorama.Style.RESET_ALL
            cellAlreadyUse = cellAlreadyUse + [cellSpawn]
            ok = True


    #generation aleatoire item qui change tous les murs du laby
    ok = False
    while ok == False:
        cellSwap = (randint(0,laby.height-1),randint(0,laby.width-1))
        if cellSwap not in cellAlreadyUse:
            affichageStuff[cellSwap] = colorama.Fore.YELLOW + '†' + colorama.Style.RESET_ALL
            cellAlreadyUse = cellAlreadyUse + [cellSwap]
            ok = True

    # generation aleatoire item qui montre le chemin le plus court de sortie pendant 3 secondes
    ok = False
    while ok == False:
        cellXRay = (randint(0, laby.height - 1), randint(0, laby.width - 1))
        if cellXRay not in cellAlreadyUse:
            affichageStuff[cellXRay] = colorama.Fore.MAGENTA + '†' + colorama.Style.RESET_ALL
            ok = True


    #affichage nombre de pas qu'on a fait
    nbPas = 0


    print(laby.overlay(affichageStuff))
    print("Tu as fait", nbPas , "pas")
    print("Nombre de pas optimaux depuis la case actuelle : ",laby.distance_geo(cell,cellFin))
    print("Appuyer sur 'H' pour commandes d'aide")

    continuer = True
    while continuer == True:
        b = False
        while b == False:
            time.sleep(0.1)
            user = keyboard.read_key()
            if user == "z" or user == "q" or user == "d" or user == "s" or user == "p" or user == "r" or user == "h" or user == "x" or user == "c":
                b = True

        temp = cell


        if user == "z" and (cell[0]-1,cell[1]) in laby.get_reachable_cells(cell):
            sound_effect = pygame.mixer.Sound('music/move.wav')
            pygame.mixer.Sound.play(sound_effect)
            print("\n")
            affichageStuff[cell] = ' '
            cell = (cell[0]-1,cell[1])
            affichageStuff[cell] = persoStr
            print(laby.overlay(affichageStuff))
            nbPas = nbPas+1



        if user == "s" and (cell[0]+1,cell[1]) in laby.get_reachable_cells(cell):
            sound_effect = pygame.mixer.Sound('music/move.wav')
            pygame.mixer.Sound.play(sound_effect)
            print("\n")
            affichageStuff[cell] = ' '
            cell = (cell[0]+1,cell[1])
            affichageStuff[cell] = persoStr
            print(laby.overlay(affichageStuff))
            nbPas = nbPas + 1



        if user == "d" and (cell[0],cell[1]+1) in laby.get_reachable_cells(cell):
            sound_effect = pygame.mixer.Sound('music/move.wav')
            pygame.mixer.Sound.play(sound_effect)
            print("\n")
            affichageStuff[cell] = ' '
            cell = (cell[0],cell[1]+1)
            affichageStuff[cell] = persoStr
            print(laby.overlay(affichageStuff))
            nbPas = nbPas + 1




        if user == "q" and (cell[0],cell[1]-1) in laby.get_reachable_cells(cell):
            sound_effect = pygame.mixer.Sound('music/move.wav')
            pygame.mixer.Sound.play(sound_effect)
            print("\n")
            affichageStuff[cell] = ' '
            cell = (cell[0],cell[1]-1)
            affichageStuff[cell] = persoStr
            print(laby.overlay(affichageStuff))
            nbPas = nbPas + 1


        # test pour savoir si le joueur est tombe sur la case cellSpawn
        if cell == cellSpawn:
            sound_effect = pygame.mixer.Sound('music/tp.wav')
            pygame.mixer.Sound.play(sound_effect)
            cell = (randint(0,laby.height-1),randint(0,laby.width-1))
            affichageStuff[cell] = persoStr
            affichageStuff[cellSpawn] = ' '
            nbPas = nbPas + 1
            affiche_tp()
            time.sleep(1.5)
            print(laby.overlay(affichageStuff))

            cellSpawn = -1

        # test pour savoir si le joueur est tombe sur la case cellSwap
        if cell == cellSwap:
            sound_effect = pygame.mixer.Sound('music/tp.wav')
            pygame.mixer.Sound.play(sound_effect)
            laby = Maze.gen_fusion(h, w)
            cellSwap = -1
            affiche_shuffle()
            time.sleep(1.5)
            print(laby.overlay(affichageStuff))




        # test pour savoir si le joueur est tombe sur la case cellXRay
        if cell == cellXRay:
            sound_effect = pygame.mixer.Sound('music/magic.wav')
            pygame.mixer.Sound.play(sound_effect)
            solution = laby.solve_dfs(cell, cellFin)
            affichageTemp = {c: colorama.Fore.CYAN + '*' + colorama.Style.RESET_ALL for c in solution}
            print(laby.overlay(affichageTemp))
            print(colorama.Fore.RED + "Affichage du chemin magique pendant 3 secondes" + colorama.Style.RESET_ALL)
            time.sleep(3)

            solution = laby.solve_dfs(cell, cellFin)
            affichageTemp = {c: ' ' for c in solution}
            affichageTemp[cell] = persoStr
            print(laby.overlay(affichageStuff))
            cellXRay = -1


        #pour recommencer le laby
        if user == "r":
            print("----------------------------------------------------------")
            clear_screen()
            print(colorama.Fore.MAGENTA + "Chargement en cours !" + colorama.Style.RESET_ALL)
            loading()
            jouer()


        #pour quitter la partie
        if user == "p":
            continuer = False

        # Afficher commandes d'aide
        if user == "h":
            affiche_help()

        # Mettre en pause la musique
        if user == "x":
            pygame.mixer.music.pause()
        elif user == "c":
            pygame.mixer.music.play(loops=-1)

        #pour voir si il a gagner:
        if cell == cellFin:
            sound_effect = pygame.mixer.Sound('music/win.wav')
            pygame.mixer.Sound.play(sound_effect)
            print(colorama.Fore.GREEN + "Tu as gagné !" + colorama.Style.RESET_ALL)
            print("Appuie sur 'N' pour lancer le nouveau labyrinthe")
            print("Appuyer sur 'H' pour commandes d'aide")
            ok = False
            while ok == False:
                user = keyboard.read_key()
                if user == "p" or user == "n":
                    ok = True
            if user == "n":
                print(colorama.Fore.MAGENTA + "Lancement du labyrinthe difficulté moyenne dans 3 secondes ! " + colorama.Style.RESET_ALL)
                time.sleep(3)
                jouerMoyen(h,w,persoStr,choixAlgo)
            if user == "p":
                continuer = False

        #info pour le joueur
        if temp != cell :
            print("Tu as fait", nbPas ,"pas au total")
            print("Nombre de pas optimaux depuis la case actuelle : ", laby.distance_geo(cell,cellFin))
            print("Appuyer sur 'H' pour commandes d'aide")


    return





def jouerMoyen(h,w,persoStr : str,choixAlgo : int):
    # choix du labyrinthe aleatoire aleatoire si le joueur à mis 0 en param
    if choixAlgo == 0:
        choixAlgo = randint(1, 3)

    # création du laby
    if choixAlgo == 1:
        laby = Maze.gen_exploration(h, w)
        print(colorama.Fore.CYAN + "Génération gen_exploration" + colorama.Style.RESET_ALL)

    elif choixAlgo == 2:
        laby = Maze.gen_fusion(h, w)
        print(colorama.Fore.CYAN + "Génération gen_fusion" + colorama.Style.RESET_ALL)

    else:
        laby = Maze.gen_wilson(h, w)
        print(colorama.Fore.CYAN + "Génération gen_wilson" + colorama.Style.RESET_ALL)


    affichageStuff = {}
    cell = (0, 0)
    cellFin = (h-1, w-1)
    affichageStuff[cell] = persoStr
    cellAlreadyUse = [cell]
    cellAlreadyUse = cellAlreadyUse + [cellFin]
    nbGem = 0
    cellGemLst = []
    cellGemLstMarque = []
    one = False

    #generation aleatoire item qui nous fais spawn aleatoirement
    ok = False
    while ok == False:
        cellSpawn = (randint(0, laby.height - 1), randint(0, laby.width - 1))
        if cellSpawn not in cellAlreadyUse:
            affichageStuff[cellSpawn] = colorama.Fore.RED + '!' + colorama.Style.RESET_ALL
            cellAlreadyUse = cellAlreadyUse + [cellSpawn]
            ok = True


    #generation aleatoire item qui change tous les murs du laby
    ok = False
    while ok == False:
        cellSwap = (randint(0,laby.height-1),randint(0,laby.width-1))
        if cellSwap not in cellAlreadyUse:
            affichageStuff[cellSwap] = colorama.Fore.YELLOW + 'S' + colorama.Style.RESET_ALL
            cellAlreadyUse = cellAlreadyUse + [cellSwap]
            ok = True

    # generation aleatoire item que nous devons recuperer pour sortir du laby
    ok = False
    while ok == False:
        cellGem = (randint(0,laby.height-1),randint(0,laby.width-1))
        if cellGem not in cellGemLst and cellGem not in cellAlreadyUse:
            affichageStuff[cellGem] = colorama.Fore.GREEN + '♦' + colorama.Style.RESET_ALL
            cellAlreadyUse = cellAlreadyUse + [cellGem]
            cellGemLst = cellGemLst + [cellGem]

        if len(cellGemLst) == 3 :
            ok = True


    #affichage nombre de pas qu'on a fait
    nbPas = 0


    print(laby.overlay(affichageStuff))
    print("Tu as fait", nbPas , "pas")
    print("Tu as", nbGem ,"/3 gemmes")
    print("Appuyer sur 'H' pour commandes d'aide")

    continuer = True
    while continuer == True:
        b = False
        while b == False:
            time.sleep(0.1)
            user = keyboard.read_key()
            if user == "z" or user == "q" or user == "d" or user == "s" or user == "p" or user == "r" or user == "h" or user == "x" or user == "c":
                b = True

        temp = cell


        if user == "z" and (cell[0]-1,cell[1]) in laby.get_reachable_cells(cell):
            sound_effect = pygame.mixer.Sound('music/move.wav')
            pygame.mixer.Sound.play(sound_effect)
            print("\n")
            affichageStuff[cell] = ' '
            cell = (cell[0]-1,cell[1])
            affichageStuff[cell] = persoStr
            print(laby.overlay(affichageStuff))
            nbPas = nbPas+1



        if user == "s" and (cell[0]+1,cell[1]) in laby.get_reachable_cells(cell):
            sound_effect = pygame.mixer.Sound('music/move.wav')
            pygame.mixer.Sound.play(sound_effect)
            print("\n")
            affichageStuff[cell] = ' '
            cell = (cell[0]+1,cell[1])
            affichageStuff[cell] = persoStr
            print(laby.overlay(affichageStuff))
            nbPas = nbPas + 1



        if user == "d" and (cell[0],cell[1]+1) in laby.get_reachable_cells(cell):
            sound_effect = pygame.mixer.Sound('music/move.wav')
            pygame.mixer.Sound.play(sound_effect)
            print("\n")
            affichageStuff[cell] = ' '
            cell = (cell[0],cell[1]+1)
            affichageStuff[cell] = persoStr
            print(laby.overlay(affichageStuff))
            nbPas = nbPas + 1




        if user == "q" and (cell[0],cell[1]-1) in laby.get_reachable_cells(cell):
            sound_effect = pygame.mixer.Sound('music/move.wav')
            pygame.mixer.Sound.play(sound_effect)
            print("\n")
            affichageStuff[cell] = ' '
            cell = (cell[0],cell[1]-1)
            affichageStuff[cell] = persoStr
            print(laby.overlay(affichageStuff))
            nbPas = nbPas + 1


        #test pour savoir si le joueur est tombe sur la case cellSpawn
        if cell == cellSpawn:
            sound_effect = pygame.mixer.Sound('music/tp.wav')
            pygame.mixer.Sound.play(sound_effect)
            cell = (randint(0, laby.height - 1), randint(0, laby.width - 1))
            affichageStuff[cell] = persoStr
            affichageStuff[cellSpawn] = ' '
            nbPas = nbPas + 1
            affiche_tp()
            time.sleep(1.5)
            print(laby.overlay(affichageStuff))
            cellSpawn = -1

        # test pour savoir si le joueur est tombe sur la case cellSwap
        if cell == cellSwap:
            sound_effect = pygame.mixer.Sound('music/tp.wav')
            pygame.mixer.Sound.play(sound_effect)
            laby = Maze.gen_fusion(h, w)
            cellSwap = -1
            affiche_shuffle()
            time.sleep(1.5)
            print(laby.overlay(affichageStuff))

        # test pour savoir si le joueur est tombe sur la case d'une gemme
        if cell in cellGemLst and cell not in cellGemLstMarque:
            sound_effect = pygame.mixer.Sound('music/gems.wav')
            pygame.mixer.Sound.play(sound_effect)
            affichageStuff[cell] = persoStr
            nbGem = nbGem+1
            cellGemLstMarque = cellGemLstMarque + [cell]

        #si il a 3 gemmes alors il peut sortir du laby
        if nbGem == 3 and one == False:
            affichageStuff[cellFin] = colorama.Fore.CYAN + '░' + colorama.Style.RESET_ALL
            print(laby.overlay(affichageStuff))
            one = True

        # pour recommencer le laby
        if user == "r":
            print("----------------------------------------------------------")
            clear_screen()
            print(colorama.Fore.MAGENTA + "Chargement en cours !" + colorama.Style.RESET_ALL)
            loading()
            jouer()

        #pour quitter la partie
        if user == "p":
            continuer = False

        # Afficher commandes d'aide
        if user == "h":
            affiche_help()

        # Mettre en pause la musique
        if user == "x":
            pygame.mixer.music.pause()
        elif user == "c":
            pygame.mixer.music.play(loops=-1)

        #pour voir si il a gagner:
        if cell == cellFin:
            if nbGem == 3:
                sound_effect = pygame.mixer.Sound('music/win.wav')
                pygame.mixer.Sound.play(sound_effect)
                affiche_end()
                print("Appuie sur 'R' pour recommencer")
                print("Appuie sur 'P' pour quitter")
                ok = False
                while ok == False:
                    user = keyboard.read_key()
                    if user == "r" or user == "p":
                        ok = True

                if user == "r":
                    print("----------------------------------------------------------")
                    clear_screen()
                    print(colorama.Fore.MAGENTA + "Chargement en cours !" + colorama.Style.RESET_ALL)
                    loading()
                    jouer()
                    
                if user == "p":
                    continuer = False
            else:
                print(colorama.Fore.YELLOW + "Il te manque",3-nbGem,"gemmes pour pouvoir prendre la sortie !" + colorama.Style.RESET_ALL)


        #info pour le joueur
        if temp != cell :
            print("Tu as fait", nbPas ,"pas au total")
            print(colorama.Fore.GREEN + "Tu as",nbGem,"/3 gemmes" + colorama.Style.RESET_ALL)
            print("Appuyer sur 'H' pour commandes d'aide")


    return




def jouerDifficle(h,w,persoStr : str,choixAlgo : int,nbPas, nbLabFini,malus):
    #choix du labyrinthe aleatoire aleatoire si le joueur à mis 0 en param
    tempChoixAlgo = -1
    if choixAlgo == 0:
        tempChoixAlgo = 0
        choixAlgo = randint(1,3)

    #création du laby
    if choixAlgo == 1:
        laby = Maze.gen_exploration(h, w)
        print("Génération gen_exploration")

    elif choixAlgo == 2 :
        laby = Maze.gen_fusion(h, w)
        print("Génération gen_fusion")

    else:
        laby = Maze.gen_wilson(h, w)
        print("Génération gen_wilson")

    if tempChoixAlgo == 0:
        choixAlgo = 0


    affichageStuff = {}
    cell = (0, 0)
    cellFin = (randint(1,h-1), randint(1,w-1))
    affichageStuff[cell] = persoStr
    affichageStuff[cellFin] = colorama.Fore.CYAN + '░' + colorama.Style.RESET_ALL
    cellAlreadyUse = [cell]
    cellAlreadyUse = cellAlreadyUse + [cellFin]
    lstCellSpawn = []
    lstCellSwap = []
    cellSpawnAlreadyUse = []
    cellSwapAlreadyUse = []

    #generation aleatoire item qui nous fais spawn aleatoirement
    ok = False
    while ok == False:
        for i in range(3):
            cellSpawn = (randint(0, laby.height - 1), randint(0, laby.width - 1))
            if cellSpawn not in cellAlreadyUse:
                affichageStuff[cellSpawn] = colorama.Fore.RED + 'o' + colorama.Style.RESET_ALL
                cellAlreadyUse = cellAlreadyUse + [cellSpawn]
                lstCellSpawn = lstCellSpawn + [cellSpawn]
        ok = True


    #generation aleatoire item qui change tous les murs du laby
    ok = False
    while ok == False:
        for i in range(3):
            cellSwap = (randint(0,laby.height-1),randint(0,laby.width-1))
            if cellSwap not in cellAlreadyUse:
                affichageStuff[cellSwap] = colorama.Fore.YELLOW + '†' + colorama.Style.RESET_ALL
                cellAlreadyUse = cellAlreadyUse + [cellSwap]
                lstCellSwap = lstCellSwap + [cellSwap]
        ok = True

    # generation aleatoire item qui montre le chemin le plus court de sortie pendant 3 secondes
    ok = False
    while ok == False:
        cellXRay = (randint(0, laby.height - 1), randint(0, laby.width - 1))
        if cellXRay not in cellAlreadyUse:
            affichageStuff[cellXRay] = colorama.Fore.MAGENTA + '†' + colorama.Style.RESET_ALL
            ok = True


    #affichage nombre de pas qu'il nous reste
    nbPasOpt = len(laby.solve_dfs(cell,cellFin))
    nbPas = nbPas + nbPasOpt + h

    #calcul du malus
    if nbLabFini % 5 == 0 and nbLabFini != 0 :
        malus = malus+1


    print(laby.overlay(affichageStuff))
    print(f"Il te reste {nbPas} pas")
    print(f"Tu as fini {nbLabFini} labyrinthe")
    print("Appuyer sur 'H' pour commandes d'aide")

    continuer = True
    while continuer == True:
        b = False
        while b == False:
            time.sleep(0.1)
            user = keyboard.read_key()
            if user == "z" or user == "q" or user == "d" or user == "s" or user == "p" or user == "r" or user == "h" or user == "x" or user == "c":
                b = True

        temp = cell


        if user == "z" and (cell[0]-1,cell[1]) in laby.get_reachable_cells(cell):
            sound_effect = pygame.mixer.Sound('music/move.wav')
            pygame.mixer.Sound.play(sound_effect)
            print("\n")
            affichageStuff[cell] = ' '
            cell = (cell[0]-1,cell[1])
            affichageStuff[cell] = persoStr
            print(laby.overlay(affichageStuff))
            nbPas = nbPas-malus



        if user == "s" and (cell[0]+1,cell[1]) in laby.get_reachable_cells(cell):
            sound_effect = pygame.mixer.Sound('music/move.wav')
            pygame.mixer.Sound.play(sound_effect)
            print("\n")
            affichageStuff[cell] = ' '
            cell = (cell[0]+1,cell[1])
            affichageStuff[cell] = persoStr
            print(laby.overlay(affichageStuff))
            nbPas = nbPas-malus



        if user == "d" and (cell[0],cell[1]+1) in laby.get_reachable_cells(cell):
            sound_effect = pygame.mixer.Sound('music/move.wav')
            pygame.mixer.Sound.play(sound_effect)
            print("\n")
            affichageStuff[cell] = ' '
            cell = (cell[0],cell[1]+1)
            affichageStuff[cell] = persoStr
            print(laby.overlay(affichageStuff))
            nbPas = nbPas-malus




        if user == "q" and (cell[0],cell[1]-1) in laby.get_reachable_cells(cell):
            sound_effect = pygame.mixer.Sound('music/move.wav')
            pygame.mixer.Sound.play(sound_effect)
            print("\n")
            affichageStuff[cell] = ' '
            cell = (cell[0],cell[1]-1)
            affichageStuff[cell] = persoStr
            print(laby.overlay(affichageStuff))
            nbPas = nbPas-malus


        #test pour savoir si le joueur est tombe sur la case cellSpawn
        if cell in lstCellSpawn and cell not in cellSpawnAlreadyUse:
            sound_effect = pygame.mixer.Sound('music/tp.wav')
            pygame.mixer.Sound.play(sound_effect)
            cellSpawnAlreadyUse = cellSpawnAlreadyUse + [cell]
            affichageStuff[cell] = ' '
            cell = (randint(0,laby.height-1),randint(0,laby.width-1))
            affichageStuff[cell] = persoStr
            nbPas = nbPas-malus
            affiche_tp()
            time.sleep(1.5)
            print(laby.overlay(affichageStuff))

        # test pour savoir si le joueur est tombe sur la case cellSwap
        if cell in lstCellSwap and cell not in cellSwapAlreadyUse:
            sound_effect = pygame.mixer.Sound('music/tp.wav')
            pygame.mixer.Sound.play(sound_effect)
            laby = Maze.gen_fusion(h, w)
            cellSwapAlreadyUse = cellSwapAlreadyUse + [cell]
            affiche_shuffle()
            time.sleep(1.5)
            print(laby.overlay(affichageStuff))
            nbPas = nbPas - malus




        # test pour savoir si le joueur est tombe sur la case cellXRay
        if cell == cellXRay:
            sound_effect = pygame.mixer.Sound('music/magic.wav')
            pygame.mixer.Sound.play(sound_effect)
            solution = laby.solve_dfs(cell, cellFin)
            affichageTemp = {c: colorama.Fore.CYAN + '*' + colorama.Style.RESET_ALL for c in solution}
            print(laby.overlay(affichageTemp))
            print(colorama.Fore.RED + "Affichage du chemin magique pendant 3 secondes" + colorama.Style.RESET_ALL)
            time.sleep(3)

            solution = laby.solve_dfs(cell, cellFin)
            affichageTemp = {c: ' ' for c in solution}
            affichageTemp[cell] = persoStr
            print(laby.overlay(affichageStuff))
            cellXRay = -1
            nbPas = nbPas - malus


        #pour recommencer le laby
        if user == "r":
            print("----------------------------------------------------------")
            clear_screen()
            print(colorama.Fore.MAGENTA + "Chargement en cours !" + colorama.Style.RESET_ALL)
            loading()
            jouer()


        #pour quitter la partie
        if user == "p":
            continuer = False

        # Afficher commandes d'aide
        if user == "h":
            affiche_help()

        # Mettre en pause la musique
        if user == "x":
            pygame.mixer.music.pause()
        elif user == "c":
            pygame.mixer.music.play(loops=-1)

        #pour voir si il a gagner:
        if cell == cellFin:
            sound_effect = pygame.mixer.Sound('music/win.wav')
            pygame.mixer.Sound.play(sound_effect)
            print(colorama.Fore.MAGENTA + "Lancement du nouveau labyrinthe dans 3 secondes ! " + colorama.Style.RESET_ALL)
            time.sleep(3)
            nbLabFini = nbLabFini+1
            jouerDifficle(h,w,persoStr,choixAlgo,nbPas,nbLabFini,malus)

        #on verifie si il n'arrive pas a 0 pas
        if nbPas <= 0:
            sound_effect = pygame.mixer.Sound('music/win.wav')
            pygame.mixer.Sound.play(sound_effect)
            affiche_end()
            print("Appuie sur 'Y' si tu veux écrire ton score")
            print("Appuie sur 'R' pour recommencer")
            print("Appuie sur 'P' pour quitter")
            ok = False
            while ok == False:
                user = keyboard.read_key()
                if user == "y":
                    name = str(input("Ecris comment veux-tu t'appeler : "))
                    score = open("score.txt", "a")
                    score.write(str(f"\n{name} : {nbLabFini} labyrinthes termines"))
                    score.close()
                    ok = True
                    continuer = False
                    jouer()

                if user == "r" :
                    clear_screen()
                    print("{:^124}".format(colorama.Fore.MAGENTA + f"Génération du labyrinthe" + colorama.Style.RESET_ALL))
                    loading()
                    jouerDifficle(15, 15, colorama.Fore.CYAN + persoStr + colorama.Style.RESET_ALL, choixAlgo, 300, 0,1)

                if user == "p":
                    continuer = False
                    ok = True
                    jouer()


        #info pour le joueur
        if temp != cell and nbPas != 0 :
            print(f"Il te reste {nbPas} pas")
            print(f"Tu as fini {nbLabFini} labyrinthe")
            print("Appuyer sur 'H' pour commandes d'aide")


    return





def jouer():

    main_menu()

    # Affichage des auteurs
    print("{:^124}".format(colorama.Fore.YELLOW + "Auteurs : Voiret Gautier & Bruzek Elouan" + colorama.Style.RESET_ALL))

    #choix du level de difficulté
    level = int(input("{:^124}".format(colorama.Fore.YELLOW + "Veuillez choisir le mode de jeu du labyrinthe (0 ou 1). Si vous choisissez 1, un labyrinthe de 15x15 sera généré et vous n'aurez qu'un certain nombre de pas limité : " + colorama.Style.RESET_ALL)))
    while level != 0 and level != 1:
        print("{:^124}".format((colorama.Fore.RED + "Vous devez choisir 0 ou 1 !" + colorama.Style.RESET_ALL)))
        clear_screen()
        level = int(input("{:^124}".format(colorama.Fore.YELLOW + "Veuillez choisir le mode de jeu du labyrinthe (0 ou 1). Si vous choisissez 1, un labyrinthe de 15x15 sera généré et vous n'aurez qu'un certain nombre de pas limité : " + colorama.Style.RESET_ALL)))

    print("{:^124}".format(colorama.Fore.MAGENTA + f"Le mode choisi est : {level} " + colorama.Style.RESET_ALL))

    # Gestion des erreurs du persoStr
    persoStr = input("{:^124}".format(colorama.Fore.YELLOW + "Veuillez choisir un caractère pour votre personnage -> ('@' est conseillé) : " + colorama.Style.RESET_ALL))
    if len(persoStr) > 1:
        persoStr = persoStr[0]
    while persoStr.isdigit():
        print("{:^124}".format((colorama.Fore.RED + "Vous devez choisir un caractère de type string !" + colorama.Style.RESET_ALL)))
        clear_screen()
        persoStr = input("{:^124}".format(
            colorama.Fore.YELLOW + "Veuillez choisir un caractère pour votre personnage -> ('@' est conseillé) : " + colorama.Style.RESET_ALL))
        if len(persoStr) > 1:
            persoStr = persoStr[0]

    # Affichage lettre choisi
    print("{:^124}".format(colorama.Fore.MAGENTA + f"La lettre choisi est : {persoStr} " + colorama.Style.RESET_ALL))

    # Gestion des erreurs du choisAlgo
    choixAlgo = int(input("{:^124}".format(colorama.Fore.YELLOW + "Veuillez choisir l'algorithme (0 pour aléatoire, 1 pour gen_exploration, 2 pour gen_fusion, 3 pour gen_wilson : " + colorama.Style.RESET_ALL)))
    while choixAlgo > 3:
        print("{:^124}".format((colorama.Fore.RED + "Vous devez choisir un algo entre 0 et 3 !" + colorama.Style.RESET_ALL)))
        clear_screen()
        choixAlgo = int(input("{:^124}".format(colorama.Fore.YELLOW + "Veuillez choisir l'algorithme (0 pour aléatoire, 1 pour gen_exploration, 2 pour gen_fusion, 3 pour gen_wilson : " + colorama.Style.RESET_ALL)))

    # Affichage algo choisi
    print("{:^124}".format(colorama.Fore.MAGENTA + f"L'algorithme choisi est : {choixAlgo} " + colorama.Style.RESET_ALL))

    if level == 0:
        # Gestion des erreurs du taille
        taille = int(input("{:^124}".format(colorama.Fore.YELLOW + "Veuillez choisir une taille pour le labyrinthe (max 15) : " + colorama.Style.RESET_ALL)))
        while taille > 15:
            print("{:^124}".format((colorama.Fore.RED + "Vous devez choisir une taille inférieur 15 !" + colorama.Style.RESET_ALL)))
            clear_screen()
            taille = int(input("{:^124}".format(colorama.Fore.YELLOW + "Veuillez choisir une taille pour le labyrinthe (max 15) : " + colorama.Style.RESET_ALL)))

        # Affichage taille choisi
        print("{:^124}".format(colorama.Fore.MAGENTA + f"La taille choisi est de : {taille} " + colorama.Style.RESET_ALL))


    clear_screen()

    # Affichage génération labyrinthe
    print("{:^124}".format(colorama.Fore.MAGENTA + f"Génération du labyrinthe" + colorama.Style.RESET_ALL))

    loading()

    if level == 0:
        jouerSimple(taille,taille,colorama.Fore.CYAN + persoStr + colorama.Style.RESET_ALL,choixAlgo)
    else:
        jouerDifficle(15,15,colorama.Fore.CYAN + persoStr + colorama.Style.RESET_ALL,choixAlgo,100,0,1)

    return

jouer()




