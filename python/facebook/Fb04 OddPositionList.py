def solution(input_list, use_enumerate=False):
    def with_range(input_list):
        result = []
        for i in range(1, len(input_list), 2):
            result.append(input_list[i])
        return result

    def with_enumerate(input_list):
        result = []
        for index, value in enumerate(input_list):
            if index % 2 == 1:
                result.append(value)
        return result

    # Choose the function based on the use_enumerate flag
    if use_enumerate:
        return with_enumerate(input_list)
    else:
        return with_range(input_list)

# Test cases
print(solution([0, 1, 2, 3, 4, 5]) == [1, 3, 5])  # Using range
print(solution([1, -1, 2, -2]) == [-1, -2])  # Using range
print(solution([0, 1, 2, 3, 4, 5], use_enumerate=True) == [1, 3, 5])  # Using enumerate
print(solution([1, -1, 2, -2], use_enumerate=True) == [-1, -2])  # Using enumerate
