# can use hashset but u will have 2 for loops and 2x memory
# why list becoz array is sorted ask if array is sorted before attempting this problem
from typing import List



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 1
        # start with left =1
        for R in range(1, len(nums)):    # R is fast pointer that increments for duplicate value
            if nums[R] != nums[R - 1]:   #new value found
                nums[L] = nums[R]        #leetcode requirement, original array changed no new array
                L += 1
        return L
nums  = [1,1,2] ;
nums2 = [0,0,1,1,1,2,2,3,3,4];
tuple = (  (nums) , (nums2)  )
# input: [1, 2, 2] result: 2
# input: [0, 1, 2, 3, 4, 2, 2, 3, 3, 4] result: 5
s = Solution()
for item in tuple:
    print("input:",item, "result:", s.removeDuplicates(item))
