# Python to find N largest elements from a list

def top_n_elements (list1,n):
      list1.sort()
      return (list1[-n:])

list1 = [9,4,23,2,11]
n = 3
print ( top_n_elements(list1,3) )