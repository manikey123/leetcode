from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, k - 1
        res = float("inf")
        
        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l, r = l + 1, r + 1
        return res
nums  = [90] ; target = 1
nums2 = [9,4,1,7]; target2 = 2
tuple = (  (nums,target) , (nums2,target2) )
# input1: ([90], 1) result: 0
# input1: ([1, 4, 7, 9], 2) result: 2
for item in tuple:
    print("input1:",item, "result:", Solution().minimumDifference(item[0], item[1]))