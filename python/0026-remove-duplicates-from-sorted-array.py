# can use hashset but u will have 2 for loops and 2x memory
# why list becoz array is sorted ask if array is sorted before attempting this problem
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 1
        # start with left =1 
        for R in range(1, len(nums)):
            if nums[R] != nums[R - 1]: # check if index0 != index1 add to left
                nums[L] = nums[R]
                L += 1
        return L
nums  = [1,1,2] ;
nums2 = [0,0,1,1,1,2,2,3,3,4];
tuple = (  (nums) , (nums2)  )
# input: ([2, 7, 11, 15], 9) result: [0, 1]
# input: ([3, 2, 4], 6) result: [1, 2]
# input: ([3, 3], 6) result: [0, 1]
s = Solution()
for item in tuple:
    print("input:",item, "result:", s.removeDuplicates(item))