from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Approach 1: Square and Sort
        # This line squares each number in the list and then sorts the resulting list

        # Initialize an empty list to store the squares
        squares = []
        # Iterate over each number in the input list
        for x in nums:
            # Square the number and append it to the squares list
            squares.append(x * x)
        # Sort the squares list
        squares.sort()
        # Return the sorted list of squares
        return squares
        # return sorted(x * x for x in nums) #LC

    def sortedSquaresTwoPointers(self, nums: List[int]) -> List[int]:
        # Approach 2: Two-Pointer Technique
        # Get the length of the input list
        n = len(nums)
        # Initialize a result list with zeros, of the same length as the input list
        result = [0] * n
        # Initialize two pointers, one at the start and one at the end of the list
        left, right = 0, n - 1
        # Iterate while the left pointer is not greater than the right pointer
        while left <= right:
            # Calculate the square of the elements at the left and right pointers
            left_square, right_square = nums[left] ** 2, nums[right] ** 2
            # Compare the squares to decide where to place the larger one in the result list
            if left_square > right_square:
                # Place the larger square at the correct position in the result list
                result[right - left] = left_square
                # Move the left pointer to the right
                left += 1
            else:
                # Place the larger square at the correct position in the result list
                result[right - left] = right_square
                # Move the right pointer to the left
                right -= 1
        # Return the result list
        return result

# Test cases
sol = Solution()
# Test with a mixed list of negative and positive numbers
assert sol.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]  # Example 1
# Test with another mixed list
assert sol.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]  # Example 2

# Additional Test Cases
# Test with a


'''
Certainly! Let's walk through the code with the input `[-4, -1, 0, 3, 10]`. The goal of this code is to return a new list where each element is the square of the corresponding element in the input list, sorted in non-decreasing order. This is achieved using a two-pointer approach.

1. **Initialize Variables**:
    - `nums = [-4, -1, 0, 3, 10]`
    - `n = 5` (length of `nums`)
    - `result = [0, 0, 0, 0, 0]` (initially filled with zeros, same length as `nums`)
    - `left = 0`, `right = 4` (pointers at the start and end of the list)

2. **Iteration 1**:
    - `left_square = nums[left] ** 2 = (-4) ** 2 = 16`
    - `right_square = nums[right] ** 2 = 10 ** 2 = 100`
    - `right_square > left_square`
    - `result[4 - 0] = 100`, so `result = [0, 0, 0, 0, 100]`
    - `right` is decremented to `3`.

3. **Iteration 2**:
    - `left_square = 16`
    - `right_square = nums[3] ** 2 = 3 ** 2 = 9`
    - `left_square > right_square`
    - `result[3 - 0] = 16`, so `result = [0, 0, 0, 16, 100]`
    - `left` is incremented to `1`.

4. **Iteration 3**:
    - `left_square = nums[1] ** 2 = (-1) ** 2 = 1`
    - `right_square = 9`
    - `right_square > left_square`
    - `result[3 - 1] = 9`, so `result = [0, 0, 9, 16, 100]`
    - `right` is decremented to `2`.

5. **Iteration 4**:
    - `left_square = 1`
    - `right_square = nums[2] ** 2 = 0 ** 2 = 0`
    - `left_square > right_square`
    - `result[2 - 1] = 1`, so `result = [0, 1, 9, 16, 100]`
    - `left` is incremented to `2`.

6. **Iteration 5**:
    - Now `left` and `right` both point to `2`.
    - `left_square = right_square = 0`
    - `result[2 - 2] = 0`, so `result = [0, 1, 9, 16, 100]`
    - `left` is incremented to `3`.

7. **End of Loop**:
    - The loop ends because `left > right` (3 > 2).

The final `result` is `[0, 1, 9, 16, 100]`, which is the sorted array of squares of the elements in `nums`.

This approach effectively places the larger of the two squared values at the correct position from the end of the `result` array, gradually filling it up in a sorted manner. The two-pointer technique is beneficial here as it allows handling negative numbers efficiently, which when squared, could be larger than the squares of positive numbers.
'''
