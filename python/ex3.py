test_list = [1, 2, 3, 4, 5]
copy_list = [[0]]

def sublists(l):
    for st in range(len(l)):
        for en in range(st + 1, len(l) + 1):
            copy_list.append(l[st:en])
            print(copy_list)


print(sublists(test_list))