from typing import List
# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
            
        return res
height   = [1,8,6,2,5,4,8,3,7]
height2 = [1,1]
tuple = (  (height) , (height2)  )
s = Solution()
for item in tuple:
    print("input:",item, "output:", s.maxArea(item))

#Results:
# input: [-4, -1, -1, 0, 1, 2] output: [[-1, -1, 2], [-1, 0, 1]]
# input: [0, 1, 1] output: []
# input: [0, 0, 0] output: [[0, 0, 0]]