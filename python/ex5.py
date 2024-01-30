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

    morse_code = morse_code[:-1] # strip the last letter of the string which will be a space

    return morse_code

print(exercise5("Hello, World!"))
print(exercise5("hello         world"))
