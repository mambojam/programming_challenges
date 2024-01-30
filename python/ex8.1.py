def exercise8(filename, line_length):
    #open file in read mode, parse text, split text into lines in list
    with open(filename, 'r') as file:
        text = file.read()
        text = text.splitlines()


    #2 for loops for lines and words
    justified_line = ""
    justified_text = []

    for line in text:
        words = line.split(" ")

        for word in words:

            if len(justified_line + word) <= line_length:
                justified_line = f"{justified_line}{word} "
                if line == text[-1] and word == words[-1]:
                    justified_text.append(justified_line.strip(" "))

            else:
                justified_text.append(justified_line.strip(" "))
                justified_line = f"{word} "
                if line == text[-1] and word == words[-1]:
                    justified_text.append(justified_line.strip(" "))

    return justified_text


print(exercise8("test_data/text1.txt", 50))