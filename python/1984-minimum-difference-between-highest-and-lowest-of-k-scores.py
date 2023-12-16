from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # Edge case checks
        if k == 1 or not nums:
            return 0

        nums.sort()  # Sort the array in ascending order.
        left, right = 0, k - 1  # Initialize pointers for the sliding window.
        min_diff = float("inf")  # Initialize the result with infinity.

        while right < len(nums):  # Iterate until the right pointer reaches the end of the array.
            min_diff = min(min_diff,
                           nums[right] - nums[left])  # Update the result with the minimum difference found so far.
            left, right = left + 1, right + 1  # Move the sliding window forward by one position.
        return min_diff  # Return the final result.


# Function to test the solution with multiple test cases
def test_solution():
    test_cases = [([90], 1), ([9, 4, 1, 7], 2)]
    for nums, k in test_cases:
        print(f"Input: {nums}, k={k}; Result: {Solution().minimumDifference(nums, k)}")


# Run the test cases
test_solution()
