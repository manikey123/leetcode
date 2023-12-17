from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow . In some languages, particularly those with fixed-size integer types (like C++ or Java), the expression (l + r) // 2 can cause an integer overflow if l and r are large enough. This is because the sum l + r could exceed the maximum value that can be stored in an integer variable.
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target: # if nums[m] < target ; discard left side ; update the left side ; l =
                l = m + 1
            else:
                return m
        return -1

# Test cases from LeetCode
sol = Solution()
assert sol.search([-1,0,3,5,9,12], 9) == 4  # Example 1
assert sol.search([-1,0,3,5,9,12], 2) == -1  # Example 2
# Additional Test Cases
assert sol.search([1, 2, 3, 4, 5], 3) == 2
assert sol.search([1, 2, 3, 4, 5], 6) == -1
assert sol.search([], 1) == -1  # Empty array