from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # O(log n) and O(1)
        
        
        low, high = 0, len(nums)
        while low<high:
            mid = low +(high - low) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low

# Test cases from LeetCode
sol = Solution()
assert sol.searchInsert([1, 3, 5, 6], 5) == 2  # Example 1
assert sol.searchInsert([1, 3, 5, 6], 2) == 1  # Example 2
assert sol.searchInsert([1, 3, 5, 6], 7) == 4  # Example 3

# Additional Test Cases
assert sol.searchInsert([1, 3, 5, 6], 0) == 0  # Target less than all elements