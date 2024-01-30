def exercise8(filename, line_length):
    #open file in read mode, parse text, split text into lines in list
    with open(filename, 'r') as file:
        text = file.read()
        text = text.splitlines()

    #create an empty string, loop through the list of lines to concatenate a single line string
    full_line = ""
    for line in text:
        full_line += line + " "

    #create a new list to move max line length lines into
    full_line_list = []

    #iterate through the characters in the string to find the characters that are multiples of the line_length
    for i in range(len(full_line)):
        new_line = ""
        if i != 0 and i % line_length == 0:

            #need to find the nearest whitespace before the max line length
            if full_line[i] != " ":
                line_end = full_line.rfind(" ", 0, i)
                print(line_end)
                # new_line = full_line[:line_end]
                # i = line_end

                # for j in range(i, 0, -1):
                #     if full_line[j] == " ":
                #         x = i - j
                #         global new_line = full_line[j-(line_length-x):j]
                #         # full_line_list.append(new_line)
                #         break
            else:
                new_line = full_line[i - line_length: i]
                # full_line_list.append(full_line[i - line_length: i])

        full_line_list.append(new_line)


    print(full_line)
    print(full_line_list)
    # for i in range(len(text)):
    #     full_line = ""
    #     full_line += text[i] + " "
    #     print(full_line)


exercise8("test_data/text1.txt", 50)
