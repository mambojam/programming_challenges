# using a dictionary to map the alphabetised columns to numbers
columns = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

# using a list of tuples to represent the 8 possible moves a Knight can make
# e.g. first tuple = along one column, up two rows
pos_moves = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]


def ex9(start, end, moves):
    # transform the input to [column, row] format as nums in list
    position = [columns[start[0]], int(start[-1])]
    end_position = [columns[end[0]], int(end[-1])]

    # create a dictionary where key = move_num and value = list of pos_positions starting move 0 = position
    pos_positions = {0: [position]}

    # limit the number of moves
    for num in range(moves):
        move_num = num + 1  # start from 1 (not 0)
        pos_positions[move_num] = []  # create a new key in the dictionary for this move

        # iterate through the positions after each move
        for pos in pos_positions[num]:
            # adding the possible moves to the start_position
            for move in pos_moves:
                new_position = [pos[0] + move[0], pos[1] + move[1]]
                # is it a match?
                if new_position == end_position:
                    return True
                # add new position to the dictionary
                elif (0 < new_position[0] <= 8
                      and 0 < new_position[1] <= 8):
                    pos_positions[move_num].append(new_position)

    return False

print(ex9("a1", "f5", 3))
print(ex9("a1", "f5", 2))
print(ex9("a1", "c2", 1))
print(ex9("a1", "b3", 1))
print(ex9("a1", "b4", 1))
print(ex9("a1", "b4", 5))
print(ex9("e4", "d3", 3))



