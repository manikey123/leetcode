from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans



nums = [1,2,1]
nums2 = [1,3,2,1]
tuple = (nums, nums2)
s = Solution()
for item in tuple:
    print("input:",item, "output:", s.getConcatenation(item))