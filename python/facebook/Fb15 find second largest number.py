# Python to find second largest number in  a list
list1=[10,20,5,9,30]
list1.sort()
print(list1[-2])

# To print even number in a list

list1 = [10, 21, 4, 45, 66, 93]
for num in list1:
      if num%2 ==0:
            print (num,end=" ")

# Method 2
even_num = [num for num in list1 if num % 2 ==0]
print (even_num)

# Print all even numbers in a range
print ("input here")



start=10
end=20
evenlist = []

for num in range(start,end+1):
    if num % 2 == 0:
        evenlist.append(num)
# print ("even",num, end= " ")
print("evenlist", evenlist)

# Print all odd number in a range
Start = 10
End = 20
oddlist = []
for num in range(start,end+1):
       if num % 2 !=0:
           oddlist.append(num)
print ("oddlist", oddlist)

# Print all odd number in a list
odd_number= [number for number in list1 if num % 2 != 0]
print (odd_number)
