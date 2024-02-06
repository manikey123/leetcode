from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i] #k is slow ; i is fast ;
                k += 1
        print("final array", nums)
        return k   #
nums  = [3,2,2,3] ; target = 3
nums2 = [0,1,2,2,3,0,4,2]; target2 = 2
tuple = (  (nums,target) , (nums2,target2)  )
# input1: ([2, 2, 2, 3], 3) result: 2              < 2 elements that are not the target 3> --> array becomes [2, 2, 2, 3]  moves behind the target 3
# input1: ([0, 1, 3, 0, 4, 0, 4, 2], 2) result: 5  < 5 elements that are not the target 2> --> array becomes [0, 1, 3, 0, 4, 0, 4, 2] moves behind out the target 2
for item in tuple:
    print("input1:",item, "result:", Solution().removeElement(item[0], item[1]))


