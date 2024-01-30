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

print(exercise7("functions.txt"))


