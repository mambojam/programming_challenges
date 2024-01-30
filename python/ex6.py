# Complete the function ‘exercise6’ that takes an integer between 0 and 999
# as its only parameter, and returns a string containing the English words for
# that number

#use dictionaries

#use a dictionary for hundreds, tens, 0-1
# if num > 10, string = tens[] + digits[] etc

digits = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
          "6": "six", "7": "seven", "8": "eight", "9": "nine", "0": ""}

teens = {"11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen",
         "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen", "0": ""}

tens = {"1": "ten", "2": "twenty", "3": "thirty", "4": "forty", "5": "fifty",
        "6": "sixty", "7": "seventy", "8": "eighty", "9": "ninety", "0": ""}

hundreds = {"1": "a hundred", "2": "two hundred", "3": "three hundred", "4": "four hundred", "5": "five hundred",
            "6": "six hundred", "7": "seven hundred", "8": "eight hundred", "9": "nine hundred", "0": ""}


def exercise6(num):
    str_num = str(num)
    spelling_out = ""

    if num == 0:
        return "zero"

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

print(exercise6(616))
print(exercise6(3))
print(exercise6(15))
print(exercise6(45))
print(exercise6(119))
print(exercise6(999))
print(exercise6(0))
print(exercise6(10))
print(exercise6(510))

