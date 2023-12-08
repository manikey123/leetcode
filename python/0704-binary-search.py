from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

# Two Variable  : 2 input rows
nums  = [-1,0,3,5,9,12] ; target = 9
nums2 = [-1,0,3,5,9,12]; target2 = 2
tuple = (  (nums,target) , (nums2,target2) )

# input1: ([-1, 0, 3, 5, 9, 12], 9) result: 4
# input1: ([-1, 0, 3, 5, 9, 12], 2) result: -1
for item in tuple:
    print("input1:",item, "result:", Solution().search(item[0], item[1]))