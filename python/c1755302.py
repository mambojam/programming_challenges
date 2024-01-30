import copy

# Exercise 1 - Smallest Fraction Terms
def exercise1(num,den):
    #  find whether num or den is lower than the other and store in
    # a variable called lower
    if num < den:
        lower = num
    elif den < num:
        lower = den
    else:
        print("That's a whole number! please enter a fraction")

    # working backwards from the lower number we'll find the greatest common divisor
    # if both num and den modulo n = 0
    for n in range(lower, 0, -1):
        if num % n == 0 and den % n == 0:
            great_com_div = n
            break
    # return the lowest common denominator
    return num/great_com_div, den/great_com_div


# Exercise 2 - Magical Dates
def exercise2(day,month,year):
    # % 100 finds the last two digits, the decade year
    if day * month == year % 100:
        return True
    else:
        return False


# Exercise 3 - All Sublists

test_list = [1, 2, 3, 4, 5] # original list
copy_list = [[]] #list to copy sublists from original list into

def exercise3(l):
    for st in range(len(l)): #have a startpoint at index 0 
        for en in range(st+1, len(l) + 1): # end point starts one ahead of start and iterates first
            copy_list.append(l[st:en]) # take slices of the string at each iteration of start and end positions
    return copy_list 



# Exercise 4 - English to Pig Latin Translator
def exercise4(word):
    punctuation = "" # to store the punctuation we strip
    punc_string = "!?.(),;:'\"-_&<>#~[]*^%$£" # the types of punctuation we're looking for
    upper = False # a switch to tell us if word starts with upperCase
    vowels = ["a", "e", "i", "o", "u"] #the vowels

    # check if the word starts with an uppercase and if it does, set upper to True and change word to lowercase
    if word[0].isupper():
        upper = True
        word = word.lower()
    # check whether the word ends in punctuation, if it does remove and store it for later
    if word[-1] in punc_string:
        punctuation += word[-1]
        word = word.strip(word[-1])
    # check whether it starts with a consonant (not a vowel)
    if word[0] not in vowels:
        consonants = "" # create somewhere to store the consonants
        for letter in word: # check each letter
            if letter not in vowels: # if the letter is a consonant
                consonants += letter # concatenate consonants string
            else:
                break # stop once we hit a vowel
        translation = word[len(consonants):] + consonants + "ay" + punctuation # slice from the end of the consonants, stick the consonants on the end and add "ay"

    else:
        translation = word + "way" + punctuation
    # if the original was capitalized, capitalize translation
    if upper:
        translation = translation.capitalize()

    return translation

# Exercise 5 - Morse Code Encoder
# create a dictionary to store all the morse_code values according to their number or letter
morse_code_dict = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": ".._", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
    "9": "----.", "0": "-----"}

def exercise5(user_input):
    # create an empty string which we will concatenate our message into
    morse_code = ""
    # convert the string to upper case
    upper_case = user_input.upper()
    # loop through the letters in the upper_case string
    for letter in upper_case:
        if letter in morse_code_dict: # if the letter exists as a key in the dictionary
            morse_code += morse_code_dict[letter] + " " # concatenate this + whitespace

    morse_code = morse_code.strip(" ") # strip the last letter of the string which will be a space

    return morse_code

# Exercise 6 - Spelling Out Numbers
# create dictionaries for the single digits, teens, tens and hundreds
digits = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
          "6": "six", "7": "seven", "8": "eight", "9": "nine", "0": ""}

teens = {"11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen",
          "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen", "0": ""}

tens = {"1": "ten", "2": "twenty", "3": "thirty", "4": "forty", "5": "fifty",
        "6": "sixty", "7": "seventy", "8": "eighty", "9": "ninety", "0": ""}

hundreds = {"1": "a hundred", "2": "two hundred", "3": "three hundred", "4": "four hundred", "5": "five hundred",
            "6": "six hundred", "7": "seven hundred", "8": "eight hundred", "9": "nine hundred", "0": ""}

def exercise6(num):
    str_num = str(num) # transform the input num to string
    spelling_out = "" # create an empty string to write the spelling out into

    if num == 0:
        return "zero"
    # check length and draw corresponding values from the dictionary keys
    length = len(str_num)
    if length == 3:
        spelling_out += hundreds[str_num[-3]] + " and "
    if length >= 2:
        if 10 < num % 100 < 20:
            spelling_out += teens[str_num[-2] + str_num[-1]]
            return spelling_out
        elif num % 100 == 10:
            spelling_out += "ten"
            return spelling_out
        else:
            spelling_out += tens[str_num[-2]] + "-"
    if length >= 1:
        spelling_out += digits[str_num[-1]]
    else:
        print("please enter a number between 0 and 999")

    return spelling_out

# Exercise 7 - No Functions without Comments
def exercise7(file):
    no_comment_funcs = []
    with open(file, 'r') as file:
        text = file.read()
        file_lines = text.splitlines()

    for i in range(len(file_lines)):
        if file_lines[i].startswith("def "):
            if not file_lines[i-1].startswith("#"):
                func_name = file_lines[i][4:]
                func_name_no_par = ""
                for char in func_name:
                    if char == "(":
                        break
                    else:
                        func_name_no_par += char
                func_name = func_name_no_par
                no_comment_funcs.append(func_name)

    return no_comment_funcs


# Exercise 8 - Justify any Text
def exercise8(filename, line_length):
    #open file in read mode, parse text, split text into lines in list
    with open(filename, 'r') as file:
        text = file.read()
        text = text.splitlines()

    #create an empty string, loop through the list of lines to concatenate a single line string
    full_line = ""
    for line in text:
        full_line += line + " "

    #list of all the words
    words = full_line.split(" ")

    #empty string to build the lines up to max length and an empty list to store lines once we reach max
    justified_line = ""
    justified_text = []

    for word in words:
        if len(justified_line + word) <= line_length:
            justified_line = f"{justified_line}{word} "
            if word == words[-1]:
                justified_text.append(justified_line.strip(" "))

        else:
            justified_text.append(justified_line.strip(" "))
            justified_line = f"{word} "
            if word == words[-1]:
                justified_text.append(justified_line.strip(" "))

    return justified_text

# Exercise 9 - Knight's Challenge
# using a dictionary to map the alphabetised columns to numbers
columns = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

# using a list of tuples to represent the 8 possible moves a Knight can make
# e.g. first tuple = along one column, up two rows
pos_moves = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]


def exercise9(start, end, moves):
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

    # if the for loop does not reach the end position in the given moves it is not possible, so return False
    return False


# Exercise 10 - War of Species

input = ["X.O", "XX.", "X.O"]
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
    neighbours = []
    for pos in neighbour_pos:
        neighbour = [cell[0] + pos[0], cell[1] + pos[1]]
        if 0 <= neighbour[0] < len(environment) and 0 <= neighbour[1] < len(environment[0]):
            neighbours.append(neighbour)

    return neighbours


def exercise10(list_of_strings):
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
            if cell == "." and 2 <= living < 6:
                if species_X_count > species_O_count:
                    cell = "X"
                else:
                    cell = "O"
            elif living > 6:
                cell = "."
            elif cell == "X" and (species_X_count < 3 or species_O_count > species_X_count):
                cell = "."
            elif cell == "O" and (species_O_count < 3 or species_X_count > species_O_count):
                cell = "."
            # populate the copy with the result
            copied_environment[i][j] = cell
    # copy the copy back to the original to change state simultaneously
    changed_env = []
    for i in range(len(copied_environment)):
        row = ""
        for column in copied_environment[i]:
            row += column
        changed_env.append(row)
    return changed_env

