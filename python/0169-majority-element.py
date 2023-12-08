from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
            
        return res


nums = [3,2,3]
nums2 = [2,2,1,1,1,2,2]
tuple = (nums , nums2)
# Input: [3, 2, 3] Output: 3
# Input: [2, 2, 1, 1, 1, 2, 2] Output: 2
for item in tuple:
    print("Input:",item, "Output:", Solution().majorityElement(item))