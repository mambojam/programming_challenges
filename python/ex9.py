# write a function that takes the start and end point on a chess board and a number of moves a knoght can make
# start and end will be in "a1", "f3" format so cut these into columns and rows and change the columns to numbers
# if using recursion, the base case will be 0 when the knight has no movement left
# create a function that runs all 8 possibilities for the knight's movement and if the start == end return true
# if the knight goes out of bounds break this function

columns = { "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
pos_moves = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]

def ex9(start, end, moves):
    start_column = columns[start[0]]
    start_row = int(start[-1])

    start_position = [start_column, start_row]
    end_position = [columns[end[0]], int(end[-1])]

    #creat a list of possible positions (might need to make one per turn)
    pos_positions = [start_position]

    #limit the number of moves
    for num in range(moves, 0, -1):
        if num == 0:
            return False
        for position in pos_positions:
            #adding the possible moves to the start_position
            for move in pos_moves:
                new_position = [position[0] + move[0], position[1] + move[1]]
                if new_position == end_position:
                    return True
                elif 0 < new_position[0] and new_position[1] <= 8:
                    pos_positions.append(new_position)



    # print(start_position)
    # start_position += 1, 1
    #
    # return start_position

    # end_column = columns[end[0]]
    # end_row = end[-1]
    #
    # if start_column == end_column and start_row == end_row:
    #     return True
    #
    # elif moves == 0:
    #     return False
    #
    #
    # def movement()
    # return start_column

print(ex9("a1", "f5", 3))
print(ex9("a1", "f5", 2))