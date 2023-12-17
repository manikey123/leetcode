class Solution:
    def isPerfectSquare2(self, num: int) -> bool:
        for i in range(1, num+1):
            if i * i == num:
                return True
            if i* i > num:
                return False

    def isPerfectSquare(self, num: int) -> bool:
        # Initialize left and right pointers for binary search
        left, right = 1, num

        # Continue the loop until left pointer is less than or equal to right pointer
        while left <= right:
            # Calculate the middle value between left and right
            mid = (left + right) // 2

            # Square the middle value
            squared = mid * mid

            # Check if the squared value is equal to the target number
            if squared == num:
                return True  # If equal, num is a perfect square
            elif squared < num:
                left = mid + 1  # If squared is less than num, search in the right half
            else:
                right = mid - 1  # If squared is more than num, search in the left half

        # Return False if no perfect square is found
        return False

# Test cases
sol = Solution()
# Test if 16 is a perfect square using both methods
assert sol.isPerfectSquare(16) == True

# Test if 14 is a perfect square using both methods
assert sol.isPerfectSquare(14) == False

# Additional Test Cases
# Test if 1 is a perfect square using both methods
assert sol.isPerfectSquare(1) == True

# Test if 2 is a perfect square using both methods
assert sol.isPerfectSquare(2) == False
