list1 = [5,3,8,9, -4]
# Count Even and odd number in a list
odd_list = [num for num in list1 if num % 2 == 1]
odd_count= len (odd_list)
Even_count = len (list1)-odd_count

print ( "positive number in a list" )

for num in list1:
    if num >= 0:
        print(num, end = ' ')


print ("Print negative number in a list")
for num in list1:
    if num < 0 :
        print (num, end =' ')
print ( "Count positive number and negative number in a list ")
for num in list1:
      positive_list = [num for num in list1 if num>=0]
      positive_list_count = len (positive_list)
      Negative_list_count = len(list1) - positive_list_count


print("val")
print ([x for x in range(100)])
print("even")

print ([x for x in range(100) if x%2==0 ])
print("odd")

print ([x for x in range(100) if x%2!=0 ])