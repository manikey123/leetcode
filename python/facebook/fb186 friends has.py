# 6 Given a two dimensional list, for example [ [2,3],[3,4],[5]] person 2 is friends with 3 etc, find how many friends each person has. Note,
# one person has no friends

def find_friends(lst):
    dct = {}
    for element1 in lst:
        for element2 in element1:
            if len(element1) != 1:
                dct[element2] = dct.get(element2, 0) + 1
            else:
                dct[element2] = 0


    return dct
lst = [ [2,3],[3,4],[5]]
print(find_friends(lst))