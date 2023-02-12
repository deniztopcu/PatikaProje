mylist = ["", [], [1, 2], [3, 4], [5, 6, 7, [8, 9, [88, 99, [1, 2, 3, 4]], 10], 11]]

reversed_list = mylist[::-1]


def reverser(liste):
    rev = liste[::-1]
    for i, elem in enumerate(rev):
        if type(elem) == list:
            reverser(elem)
        elif i == (len(rev) - 1) and type(elem) != list:
            finder(reversed_list, liste)
    return reversed_list


def finder(liste, target):
    for i, elem in enumerate(liste):
        if target == elem:
            liste[i] = target[::-1]
            break
        else:
            for index, e in enumerate(liste):
                if type(e) == list:
                    liste[index] = finder(e, target)
    return liste

print(reverser(mylist))
