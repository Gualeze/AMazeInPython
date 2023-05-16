from main import *

laby = Maze(4, 4, empty=False)
print(laby.info())
print(laby)

laby.remove_wall((0,0), (0,1))
print(laby)

laby.add_wall((0,0), (0,1))
laby.add_wall((0,1), (1,1))
print(laby)

print(laby.get_walls())

laby.fill()
print(laby)
laby.emptyFunction()
print(laby)


laby.emptyFunction()
laby.add_wall((0, 0), (0, 1))
laby.add_wall((0, 1), (1, 1))
print(laby)
print(laby.get_reachable_cells((0,1)))

laby = laby.gen_btree(15,15)
print("test btree")
print(laby)

laby = laby.gen_sidewinder(15,15)
print("test sidewinder")
print(laby)

laby = Maze.gen_fusion(15,15)
print("test gen_fusion")
print(laby)

laby = Maze.gen_exploration(15,15)
print("test gen_exploration")
print(laby)

laby = Maze.gen_wilson(15,15)
print("test gen_wilson")
print(laby)

laby = Maze(4,4, empty = True)
print(laby.overlay({
    (0, 0):'c',
    (0, 1):'o',
    (1, 1):'u',
    (2, 1):'c',
    (2, 2):'o',
    (3, 2):'u',
    (3, 3):'!'}))


laby = Maze(4,4, empty = True)
path = {(0, 0): '@',
        (1, 0): '*',
        (1, 1): '*',
        (2, 1): '*',
        (2, 2): '*',
        (3, 2): '*',
        (3, 3): '§'}
print(laby.overlay(path))

laby = Maze.gen_fusion(15,15)
solution = laby.solve_dfs((0, 0), (14, 14))
print("test solve_dfs : ")
str_solution = {c:'*' for c in solution}
str_solution[( 0,  0)] = 'D'
str_solution[(14, 14)] = 'A'
print(laby.overlay(str_solution))

solution = laby.solve_bfs((0,0),(14,14))
print("test solve_bfs : ")
str_solution = {c:'*' for c in solution}
str_solution[( 0,  0)] = 'D'
str_solution[(14, 14)] = 'A'
print(laby.overlay(str_solution))

solution = laby.solve_rhr((0,0),(14,14))
print("test solve_rhr : ")
str_solution = {c:'*' for c in solution}
str_solution[( 0,  0)] = 'D'
str_solution[(14, 14)] = 'A'
print(laby.overlay(str_solution))


nbpas = laby.distance_geo((0,0),(14,14))
print(f"test distance_geo :\n{nbpas}")
print(f"\ntest distance_man :\n{laby.distance_man((0,0),(14,14))}\n")

test = Maze.comparer_algo(5)
print(test)
