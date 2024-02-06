def solution(input):
    c = str(input)
    int_list = []
    for i in range(len(c)):
        int_list.append(int(c[i]))
    print(int_list)
    return int_list

assert solution(400) == [4, 0, 0]
assert solution(123) == [1, 2, 3]


def solution(number):
    if number == 0:
        return [0]  # Handle the case where the number is 0
    digits = []
    while number > 0:
        digit = number % 10  # Get the least significant digit
        digits.append(digit)  # Add the digit to the list
        number = number // 10  # Remove the least significant digit from the number

    return digits[::-1]  # Reverse the list to get the digits in the original order

# Test cases
assert solution(123) == [1, 2, 3]
assert solution(400) == [4, 0, 0]

def solution(number):
    if number == 0:
        return [0]  # Handle the case where the number is 0
    digits = []
    num_str = str(number)  # Convert number to string to count digits
    num_digits = len(num_str)  # Get the number of digits

    for _ in range(num_digits):
        digit = number % 10  # Get the least significant digit
        digits.append(digit)  # Add the digit to the list
        number = number // 10  # Remove the least significant digit from the number

    return digits[::-1]  # Reverse the list to get the digits in the original order

# Test cases
assert solution(123) == [1, 2, 3]
assert solution(400) == [4, 0, 0]
