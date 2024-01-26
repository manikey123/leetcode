# Remove empty tuples from a list

def remove_empty_tuples (val):
    res = []
    for item in val:
        if type(item) ==tuple and len(item) == 0:
            continue
        else:
            res.append(item)

    return res


ls = [ 1, 2, (4,5,6), 10, (), 'cow' ]
print("res",remove_empty_tuples(ls))

