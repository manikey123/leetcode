from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)  # O(n)

        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1

s = [1,7,3,6,5,6]
s2 = [1,2,3]
s3 = [2,1,-1]
tuple = (s , s2, s3)
# Input: [1, 7, 3, 6, 5, 6] Output: 3
# Input: [1, 2, 3] Output: -1
# Input: [2, 1, -1] Output: 0
for item in tuple:
    print("Input:",item, "Output:", Solution().pivotIndex(item))