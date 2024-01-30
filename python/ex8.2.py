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
    print(words)

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


print(exercise8("test_data/text1.txt", 50))