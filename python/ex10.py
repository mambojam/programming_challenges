# a list of equal length lists to represent a grid
# 2 species "X" and "0". Empty "."
# create rules depending on population of neighbouring cells
# e.g in a grid or 3 lists of three items each - grid cell grid[1][1] is surrounded by
# grid[0][0], grid[0][1], grid[0][2], grid[1][0], grid[1][2], grid[2][0], grid[2][1], grid[2][2]
# these 8 possible neighbours can be found by adding one, subtracting one or keeping the same to both
# column and row

## 2-D arrays***
# conway's game of life
# input is a list of strings not a list of lists
grid = [["X", "X", ".", ".", ".", ".", ".", "."],
        ["X", "X", ".", ".", ".", ".", "0", "."],
        [".", ".", ".", ".", ".", "0", "0", "0"]]

neighbour_pos = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

empty = "."
species_X = "X"
species_O = "O"


# for row in grid:
#     for cell in row:
#         print(cell)

def find_neighbours(cell):
    neighbours = []
    for i in range(len(neighbour_pos)):
        neighbours.append([cell[0] + neighbour_pos[i][0], cell[1] + neighbour_pos[i][1]])
    print(neighbours)

print(find_neighbours([1, 1]))



# An empty cell becomes non-empty if it is surrounded by at least two
# individuals of the same species. In particular, it becomes an individual
# of the most frequent species in its neighbourhood. In case of a draw
# between the species, the cell remains empty.

# • A non-empty cell becomes empty if it is surrounded by more than six
# non-empty cells, regardless of their species.

# • A non-empty cell becomes empty if it is surrounded by less than three
# members of its species.
# • A non-empty cell becomes empty if it is surrounded by more members
# of the opposite species than members of its species.
# • In any other circumstances, a cell does not change its value.


# def exercise10():
