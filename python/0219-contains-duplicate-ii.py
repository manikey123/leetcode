from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
nums  = [1,2,3,1] ; target = 3
nums2 = [1,0,1,1]; target2 = 1
nums3 = [1,2,3,1,2,3] ; target3 = 2
tuple = (  (nums,target) , (nums2,target2) , (nums3,target3) )
# input1: ([1, 2, 3, 1], 3) result: True
# input1: ([1, 0, 1, 1], 1) result: True
# input1: ([1, 2, 3, 1, 2, 3], 2) result: False
for item in tuple:
    print("input1:",item, "result:", Solution().containsNearbyDuplicate(item[0], item[1]))