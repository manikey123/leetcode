def solution(input):
    cu_list = []
    length = len(input)
    cu_list = [sum(input[0:x:1]) for x in range(0, length + 1)]
    return cu_list[1:]
def solution2(input):
    cu_list = []
    sum = 0
    reslist = []
    length = len(input)
    for i in range(0, length ):
        sum = sum + input[i]
        reslist.append(sum)
    return reslist

print ( solution([1, 1, 1]) == [1, 2, 3] )
print ( solution( [1, -1, 3]) == [1, 0, 3] )
print( "sol2",solution2([1, 1, 1]) )
print ( solution2([1, 1, 1]) == [1, 2, 3] )
print (solution2([1, -1, 3]) == [1, 0, 3])
