# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumberIterative(self, n: int) -> int:
        left, right = 1, n  # Initialize search range
        while left <= right:  # Continue until range is valid
            mid = (left + right) // 2  # Find the middle value
            res = guess(mid)  # Call the guess API
            if res == 0:  # Found the number
                return mid
            elif res < 0:  # Number is lower, adjust right boundary
                right = mid - 1
            else:  # Number is higher, adjust left boundary
                left = mid + 1
        return -1  # Number not found

    def guessNumberRecursive(self, n: int) -> int:
        # Define a helper function for recursive binary search
        def helper(left, right):
            # Base case: if the search range is invalid, return -1
            if left > right:
                return -1

            # Calculate the middle index of the current search range
            mid = (left + right) // 2

            # Call the guess API with the middle index
            res = guess(mid)

            # If the guess API returns 0, the correct number is found
            if res == 0:
                return mid
            # If the guess API returns -1, the target number is lower than the guess
            # Recursively search in the left half of the current range
            elif res < 0:
                return helper(left, mid - 1)
            # If the guess API returns 1, the target number is higher than the guess
            # Recursively search in the right half of the current range
            else:
                return helper(mid + 1, right)

        # Start the recursive search from 1 to n
        return helper(1, n)


# Test cases
sol = Solution()
# Assuming guess API is defined and works as expected
# The results of these tests depend on the implementation of the `guess` function

# Mock the guess API for testing
def guess(num: int) -> int:
    pick = Solution.pick  # This should be set for each test case
    if num == pick:
        return 0
    elif num < pick:
        return 1
    else:
        return -1

# Test cases
sol = Solution()

# Test Case 1: pick = 6, n = 10
Solution.pick = 6
assert sol.guessNumberIterative(10) == 6
assert sol.guessNumberRecursive(10) == 6

# Test Case 2: pick = 1, n = 1
Solution.pick = 1
assert sol.guessNumberIterative(1) == 1
assert sol.guessNumberRecursive(1) == 1

# Test Case 3: pick = 1, n = 2
Solution.pick = 1
assert sol.guessNumberIterative(2) == 1
assert sol.guessNumberRecursive(2) == 1

# Additional Test Cases
# Test Case 4: pick = 50, n = 100
Solution.pick = 50
assert sol.guessNumberIterative(100) == 50
assert sol.guessNumberRecursive(100) == 50

# Test Case 5: pick = 25, n = 50
Solution.pick = 25
assert sol.guessNumberIterative(50) == 25
assert sol.guessNumberRecursive(50) == 25

# Test Case 6: pick = 2, n = 3
Solution.pick = 2
assert sol.guessNumberIterative(3) == 2
assert sol.guessNumberRecursive(3) == 2