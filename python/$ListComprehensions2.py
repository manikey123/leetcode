#LC : (0777
nums = [6, 5, 0, 4, 9, -2] ;
# [expression for item in iterable]
squaresList  = [x * x for x in nums] ; print("squares",squaresList) #[16, 1, 0, 9, 100]
# [expression for item in iterable if condition] #if condition filters on iterable , records lost
positiveNum = [x for x in nums if x > 0] ; print("positiveElseRemoved", positiveNum )# [3, 10]
# [expression if condition for item in iterable ] #if condition filters on expression , no records lost
positiveNum = [no if no > 0 else 0 for no in nums] ; print("positiveElseZero", positiveNum) # [0, 0, 0, 3, 10] #else condition is mandatory

print("nums0", nums, "sortedFuncView not change original num:", sorted(nums), "numsB", nums, "reverseSorted", sorted(nums,reverse=True) , "numsC", nums )
      # "reversedInplace", nums.sort(reverse=True) , "numsRev", nums)
print("nums.sort returns None but does does inplace sort:", nums.sort() , "nums got sorted:", nums , nums.sort(reverse=True), "reversedNums", nums)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for row in matrix for num in row]
print("flatlist", flat_list) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
for row in matrix:
    for num in row:
        flat_list.append(num)
print("flatlist", flat_list)

#Application:
words = ["Hello", "World", "Python"]
lower_case = [word.lower() for word in words] # Output: ['hello', 'world', 'python']

squares = []
# Iterate over each number in the input list
for no in nums:
    squares.append(no * no)     # Square the number and append it to the squares list
print ("squares" , squares)
print("squaresList",sorted(squaresList))

print("sorted", sorted(x * x for x in nums))
print("sortedListed", sorted([x * x for x in nums]))

squares = [i**2 for i in range(10)] ; print("squares", squares) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


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





