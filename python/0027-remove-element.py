from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
nums  = [3,2,2,3] ; target = 3
nums2 = [0,1,2,2,3,0,4,2]; target2 = 2
tuple = (  (nums,target) , (nums2,target2)  )
# input1: ([2, 2, 2, 3], 3) result: 2
# input1: ([0, 1, 3, 0, 4, 0, 4, 2], 2) result: 5
for item in tuple:
    print("input1:",item, "result:", Solution().removeElement(item[0], item[1]))