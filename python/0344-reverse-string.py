def reverseString(s):
    """
    Reverses the characters of the array s in place.

    Args:
    s (List[str]): The array of characters to be reversed.

    Returns:
    None: The function modifies the array in place and does not return anything.
    """
    left, right = 0, len(s) - 1  # Initialize two pointers

    while left < right:
        s[left], s[right] = s[right], s[left]  # Swap the elements
        left, right = left + 1, right - 1  # Move the pointers towards the center

# Test cases
test_cases = [
    ["h", "e", "l", "l", "o"],  # Example 1
    ["H", "a", "n", "n", "a", "h"],  # Example 2
    ["a"],  # Single character
    [],  # Empty array
    ["r", "a", "c", "e", "c", "a", "r"]  # Odd number of characters
]

for test in test_cases:
    reverseString(test)
    print(test)
