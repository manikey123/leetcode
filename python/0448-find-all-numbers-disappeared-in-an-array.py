from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])

        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res

s = [4,3,2,7,8,2,3,1]
s2 = [1,1]
tuple = (s , s2)
# Input: [-4, -3, -2, -7, 8, 2, -3, -1] Output: [5, 6]
# Input: [-1, 1] Output: [2]
for item in tuple:
    print("Input:",item, "Output:", Solution().findDisappearedNumbers(item))