def solution(input):
    c = []
    for i in range(1, len(input), 2):
        c.append(input[i])
    return c


print( solution([0, 1, 2, 3, 4, 5]) == [1, 3, 5] )
print( solution([1, -1, 2, -2]) == [-1, -2] )

# assert solution([0, 1, 2, 3, 4, 5] == [1, 3, 5])
# assert solution([1, -1, 2, -2]) == [-1, -2]
