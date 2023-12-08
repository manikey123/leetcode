from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        flag = True
        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                flag = not flag
        
        return 1 if flag else -1
s = [-1,-2,-3,-4,3,2,1]
s2 = [1,5,0,2,-3]
s3 = [-1,1,-1,1,-1]
tuple = (s , s2, s3)
# Input: [-1, -2, -3, -4, 3, 2, 1] Output: 1
# Input: [1, 5, 0, 2, -3] Output: 0
# Input: [-1, 1, -1, 1, -1] Output: -1
for item in tuple:
    print("Input:",item, "Output:", Solution().arraySign(item))