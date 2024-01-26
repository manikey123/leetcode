# Print duplicates from a list of integer
l=[1,2,2,3,4,5]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
else :
    print (i,end= " ")
