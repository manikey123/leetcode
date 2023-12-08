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

nums  = [1,3,5,6] ; target = 5
nums2 = [1,3,5,6]; target2 = 2
nums3 = [1,3,5,6] ; target3 = 7
tuple = (  (nums,target) , (nums2,target2) , (nums3,target3) )
# input: ([1, 3, 5, 6], 5) result: 2
# input: ([1, 3, 5, 6], 2) result: 1
# input: ([1, 3, 5, 6], 7) result: 4
for item in tuple:
    print("input:",item, "result:", Solution().searchInsert(item[0], item[1]))