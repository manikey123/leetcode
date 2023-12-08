# Time: O(n), one pass using two pointers.
# Space: O(1), output array is not considered for space complexity.
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1
        
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                res[r - l] = left * left
                l += 1
            else:
                res[r - l] = right * right
                r -= 1
        return res

s = [-4,-1,0,3,10]
s2 = [-7,-3,2,3,11]
tuple = (s , s2)
# Input: ['flower', 'flow', 'flight'] Output: fl
# Input: ['dog', 'racecar', 'car'] Output:
for item in tuple:
    print("Input:",item, "Output:", Solution().sortedSquares(item))
