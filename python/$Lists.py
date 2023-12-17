#A01 Python Lists
#A02 String
#A03 Dictionary


#A01 Python Lists
myList = [3, 1, 4, 1, 7, 5, 9, 7, 2, 7]
print( "len" , len(myList) , "max", max(myList), "min", min(myList) , sum(myList))
myList.append(91)
myList.extend([92, 93,94]) #needs iterable cannot be int
myList.remove(93) #removes the first occurance
print("list updated",myList)
myList.pop(2) #Removes and returns the element at a specific index.
print("list updated  after pop at index 2 ",myList)
myList.index(2)
print("Returns the index of the first occurrence of a specified value - 9 occurs at position 5 using index of 9 .", myList.index(9)  ,
      "7 occurs 3 times in the list", myList.count(7) )


print("Sorting functions : 01 list sort ", myList.sort())
print ("my list", myList)
my_list = [6, 5, 3, 8, 5, 1]
myList2 = my_list.sort(reverse=True )
print("Sorting functions : 01b list sort ", myList2, my_list)  #.sort does inplace replacement. it does not return value.


print("02 list reverse ", myList.reverse())
print ("my list", myList)
print(" 03 sorted list  function ", sorted(myList)) # sorts
print ("my list", myList) #loses the sort
myList = [3, 1, 4, 1, 7, 5, 9, 7, 2, 7]
print(" 04 reversed list function" , reversed(myList)) # generate object, no value
print ("my list", myList)
print(" 05 reverse list ", myList[::-1])
print("mylist", myList) #not impact base list

myList = [6,5,0,4,9,2,0,2,8,6]

print("slicing",myList[1:4]) #slicing for elements at index 1,2,3, --> 504


# List Comprehension : Input: Numbers from 0 to 9
# Output: Squares of each number
squares = []
# Using a regular for loop
for x in range(10):
    squares.append(x**2)
# Print the result
print(squares)

# Input: Numbers from 0 to 9
# Output: Squares of each number
squares = [x**2 for x in range(10)]
print(squares)


print ( "zip list ",  list(zip([1, 2, 3, 4], ['a', 'b', 'c'])) ) #zip function stops at the shorter string
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c']
result = []

for i in range(min(len(list1), len(list2))): # Using a loop to combine elements from both lists
    result.append((list1[i], list2[i]))
print(result)


my_list = ['apple', 'banana', 'cherry', 'date']
for i, s in enumerate(my_list): # Using enumerate to iterate over the list
    print(f"Index: {i}, Element: {s}")


#A02 String

s = "Hello, World!"
print( "string #A02 String", len(s), s.lower(), s.upper())
s = "Hello, World!"
print("replace directly ", s.replace("World", "Python"))
print("S after direct replace",s)
s= s.replace("World", "Python")
print("replace assigning same variable:",s)



my_string = "apple,orange,banana"
fruit_list = my_string.split(",") #Splits a string into a list of substrings based on a specified delimiter.
print(fruit_list , "type", type(fruit_list)) , fruit_list[0]  # Output: ['apple', 'orange', 'banana']
x , y , z = my_string.split(",")
print( "x y z fruits ", x, y, z )

my_string = "   Hello, World!   "
stripped_string = my_string.strip()
print(stripped_string)  # Output: Hello, World!


my_list = ['apple', 'orange', 'banana'] # join(): Joins elements of an iterable (like a list) into a single string.
my_string = ",".join(my_list)
print("join", my_string)  # Output: apple,orange,banana


my_string = "Hello, World!"
starts_with_hello = my_string.startswith("Hello")
ends_with_world = my_string.endswith("World")
print(starts_with_hello)  # Output: True
print(ends_with_world)  # Output: False

#A03 Dictionary

# Creating an empty dictionary
my_dict = {}

# Adding key-value pairs
my_dict['name'] = 'John'
my_dict['age'] = 30
my_dict['city'] = 'New York'
# Displaying the dictionary
print(my_dict)



my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
keys_list = my_dict.keys()
print(keys_list )  # Output: dict_keys(['name', 'age', 'city'])

values_list = my_dict.values()
print(values_list)  # Output: dict_values(['John', 25, 'New York'])


#getting data from dictionary

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# Using square bracket notation
value = my_dict['key2']
print("value:")

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Using get() method
value = my_dict.get('key2')                   #value2
value = my_dict.get('keyx')   ; print(value)  #none
value = my_dict.get('keyx',0) ; print(value)  #0

#A04 2 D Array


l = [6, 5, 3, 8, 5, 1]
# Sort the list in descending order
sorted_list = sorted(l, reverse=True)
# Take the top two elements
top_two_elements = sorted_list[:2]
# Display the top two elements
print("Top two elements:", top_two_elements)


my_list = [6, 5, 3, 8, 5, 1]

# Sort the list in reverse order using sorted function
sorted_list = sorted(my_list, reverse=True)

# Display the sorted list in reverse order
print("Top two elements:", sorted_list[:2])

#Using nlargest from heapq module:
import heapq

l = [6, 5, 3, 8, 5, 1]

# Find the top two elements using heapq.nlargest
top_two_elements = heapq.nlargest(2, l)

# Display the top two elements
print("Top two elements using heapq.nlargest:", top_two_elements)

#Using max function twice:

l = [6, 5, 3, 8, 5, 1]

# Find the maximum element
max_element = max(l)

# Remove the maximum element and find the new maximum element (second highest)
l.remove(max_element)
second_max_element = max(l)

# Display the top two elements
print("Top two elements using max function twice:", [max_element, second_max_element])

nums = [-4, -1, 0, 3, 10]
n = len(nums)
# Initialize a result list with zeros, of the same length as the input list
result = [0] * n
print ("result", result )