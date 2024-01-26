

x =[None, None, 1, 2, None, None, 3, 4, None, 5, None, None]
for i,e in enumerate(x[:-1], 1):
    if x[i] is None:
        x[i] = x[i-1]
print(x)



def none_replace(ls):
    p = None
    return [p:=e if e is not None else p for e in ls]

ls = [None, None, 1, 2, None, None, 3, 4, None, 5, None, None]
print( none_replace(ls) )



x =[None, None, 1, 2, None, None, 3, 4, None, 5, None, None]
for i in range(len(x)):
    if x[i] is None:
       x[i] =x[i-1]
print(x)
