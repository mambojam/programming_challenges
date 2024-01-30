# transform input of list of strings into a 2-d array, list of lists
# check what the values of the neighbours are - can use counters for X, . , 0
# need to stop it from going out of bounds e.g if index is > 0, check -1 or less than 8 check +1
# check counters living, X , 0, dead - which is greatest
# if 2 < living < 6, if X < Y: cell = Y, elif X > Y = X
# if living < 3 or living >= 6 cell = empty
# if cell = X and Y_Count > X_count cell = empty (and vice versa)
# if = empty AND X_counter or 0_counter >= 2 becomes not empty
import copy

input = ['XX......', 'XX....O.', '.....OOO']
new_env = []

def two_d_array(list_of_strings):
    for strg in list_of_strings:
        str_lst = []
        for char in strg:
            str_lst.append(char)
        new_env.append(str_lst)
    
    return new_env

neighbour_pos = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def find_neighbours(cell, environment):
    """ takes the current cell co-ordinates and the grid environment as parameters
    and creates a list of neighbouring cell co-ordinates providing they are within range 
    0 to number of rows (len(environment)) and 0 to number of columns (len(environment[0]))
     """
    neighbours = []
    for pos in neighbour_pos:
        neighbour = [cell[0] + pos[0], cell[1] + pos[1]]
        if 0 <= neighbour[0] < len(environment) and 0 <= neighbour[1] < len(environment[0]):
            neighbours.append(neighbour)

    return neighbours

def ex10(list_of_strings):
    # turn the list of strings into a 2d array
    new_env = two_d_array(list_of_strings) 

    # create a copy of the environment
    copied_environment = copy.deepcopy(new_env)

    # loop through each list and each list item
    for i in range(len(new_env)):
        for j in range(len(new_env[i])):
            # keep count of the neighbouring X and O values
            species_X_count = 0
            species_O_count = 0
            # give the current thing y and x co-ordinates
            cell = [i, j]
            # find neighbours
            neighbours = find_neighbours(cell, new_env)
            # count the number of different neighbouring species
            for neighbour in neighbours:
                y = neighbour[0]
                x = neighbour[1]
                if new_env[y][x] == "X":
                    species_X_count += 1
                elif new_env[y][x] == "O":
                    species_O_count += 1
            living = species_O_count + species_X_count
            # look at the current cell again
            cell = new_env[i][j]
            # check the conditions
            if 2 <= living < 6:
                if species_X_count > species_O_count:
                    cell = "X"
                elif species_O_count > species_X_count:
                    cell = "O"
            elif living > 6:
                cell = "."
            elif cell == "X" and (species_X_count < 3 or species_O_count > species_X_count):
                cell = "."
            elif cell == "O" and (species_O_count < 3 or species_X_count > species_O_count):
                cell = "."
            # populate the copy with the result
            copied_environment[i][j] = cell
# copy the copied environment and return to list of strings format    
    changed_env = []
    for i in range(len(copied_environment)):
        row = ""
        for column in copied_environment[i]:
            row += column
        changed_env.append(row)
    print(input)
    return changed_env




            # if 2 < living < 6, if X < Y: cell = Y, elif X > Y = X
            # if living < 3 or living >= 6 cell = empty
            # if cell = X and Y_Count > X_count cell = empty (and vice versa)
            # if = empty AND X_counter or 0_counter >= 2 becomes not empty

    # # adds the co-ordinates to the grid
    # for i in range(len(new_env)):
    #     for j in range(len(new_env[i])):
    #         new_env[i][j] = (new_env[i][j], i+1, j+1)
    #
    #
    # return new_env



print(ex10(input))



