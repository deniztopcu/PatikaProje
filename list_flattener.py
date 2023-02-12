mylist = [[["fish"], 1, 'a', ['cat'], 2], [""], [[[3, [4, 5, [6, 7, [["bird"]]]]]], 'dog'], 8, 9]


restart = True
while restart:
    for i in mylist:
        if type(i) == list:
            mylist[mylist.index(i):mylist.index(i) + 1] = [j for j in i]
            break
        else:
            type_list = [str(type(elem)) for elem in mylist]
            if type_list.count("<class 'list'>") == 0:
                restart = False
print(mylist)


# mylist = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
#
# flatten_list = []
# def flatten(liste):
#     for i in liste:
#         if type(i) == list:
#             flatten(i)
#         else:
#             flatten_list.append(i)
#
#     return flatten_list
#
# print(flatten(mylist))

