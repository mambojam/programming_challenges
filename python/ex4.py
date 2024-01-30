# variable for punctuation (empty string) and variable for upper False
# need to remove punctuation - if there is then save this in a variable and remove
# check if first letter is upper case - if there is then save this in a boolean is letter A <= letter <= Z
# need to lowercase .lower() -
# capitalize IF there is a capital first letter -- set upper case to True
# if first letter is vowel - add way to end of word
# find the first vowel; slice the prefix, add to the end of word; add 'ay'
# if upcase = True, then capitalize
# add punctuation to the end

def pig_latin_translate(word):
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
        translation = word[len(consonants):] + consonants + "ay" + punctuation  # slice from the end of the consonants, stick the consonants on the end and add "ay"
    else:
        translation = word + "way" + punctuation
    # if the original waas capitalized, capitalize translation
    if upper:
        translation = translation.capitalize()

    return translation


print(pig_latin_translate("Hello."))
print(pig_latin_translate("Arranges?"))
print(pig_latin_translate("Cream"))
print(pig_latin_translate("rhythm"))
print(pig_latin_translate("Lynx!"))
print(pig_latin_translate("Galsdair"))






