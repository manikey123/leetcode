from typing import List 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
s = Solution()
nums  = [2,7,11,15] ; target = 9
nums2 = [3,2,4]; target2 = 6
nums3 = [3,3] ; target3 = 6
tuple = (  (nums,target) , (nums2,target2) , (nums3,target3) )
for item in tuple:
    print("input:",item, "result:", s.twoSum(item[0], item[1]))