def solution(input):
    c = str(input)
    int_list = []
    for i in range(len(c)):
        int_list.append(int(c[i]))
    print(int_list)
    return int_list

assert solution(400) == [4, 0, 0]
assert solution(123) == [1, 2, 3]

# assert solution([1, 1, 1]) == [1, 2, 3]
# assert solution([1, -1, 3]) == [1, 0, 3]
