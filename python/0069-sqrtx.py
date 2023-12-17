class Solution:
    def mySqrt_binary_search(self, x: int) -> int:
        # Binary Search Approach
        # If x is less than 2, its square root is x itself (0 or 1).
        if x < 2:
            return x

        # Initialize the left and right pointers for binary search.
        # The square root of x will be between 2 and x // 2.
        left, right = 2, x // 2

        # Perform binary search.
        while left <= right:
            # Calculate the midpoint to avoid overflow.
            mid = left + (right - left) // 2
            # Square of the midpoint.
            num = mid * mid

            # If the square is greater than x, move the right pointer.
            if num > x:  #greater than target fix the right
                right = mid - 1
            # If the square is less than x, move the left pointer.
            elif num < x:
                left = mid + 1
            # If the square is equal to x, return the midpoint.
            else:
                return mid

        # Return the right pointer, which is the integer part of the square root.
        return right


# Test cases
sol = Solution()
# Test with example 1: Should return 2 as the square root of 4.
print(sol.mySqrt_binary_search(4))
# Test with example 2: Should return 2 as the integer part of the square root of 8.
print(sol.mySqrt_binary_search(8))

