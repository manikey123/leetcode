#LC : (0777
# [expression for item in iterable]
nums = [-4, -1, 0, 3, 10] ; squaresList  = [x * x for x in nums] ; print("sqList",squaresList) #[16, 1, 0, 9, 100]
# [expression for item in iterable if condition] #if condition filters on iterable , records lost
even_numbers = [x for x in range(20) if x % 2 == 0] ; print("even_numbers", even_numbers)# Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18] ;
# [expression if condition for item in iterable ] #if condition filters on expression , no records lost
nums = [-4, -1, 0, 3, 10] ; squaresList  = [x * x for x in nums] ; print("sqList",squaresList) #[16, 1, 0, 9, 100]

print("squaresList",squaresList, "sorted2",sorted(squaresList), " originalList not affected ", squaresList )
print("sorted function returns None:", squaresList.sort(), "generates sorted list when printed", squaresList, "end")
squares = []
# Iterate over each number in the input list
for no in nums:
    squares.append(no * no)     # Square the number and append it to the squares list
print ("squares" , squares)
print("squaresList",sorted(squaresList))

print("sorted", sorted(x * x for x in nums))
print("sortedListed", sorted([x * x for x in nums]))

squares = [i**2 for i in range(10)] ; print("squares", squares) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for row in matrix for num in row]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("flatlist", flat_list)

for row in matrix:
    for num in row:
        flat_list.append(num)

print("flatlist", flat_list)

values = [10, 20, -5, 30]
adjusted = [no if no > 0 else 0 for no in values]
# Output: [10, 20, 0, 30]

values = [10, 20, -5, 30]
adjusted = []

for x in values:
    if x > 0:
        adjusted.append(x)
    else:
        adjusted.append(0)

# Output: [10, 20, 0, 30]

values = [10, 20, -5, 30]
adjusted2 = [x  if x > 0  else 0  for x in values]
print("adjusted2", adjusted2)


words = ["Hello", "World", "Python"]
lower_case = [word.lower() for word in words]
# Output: ['hello', 'world', 'python']


