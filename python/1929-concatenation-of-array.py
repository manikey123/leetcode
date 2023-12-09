from typing import List

# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         return nums+nums
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):  # range(2) --> 0 , 1
            for n in nums:
                ans.append(n)
        return ans



nums = [1,2,1]
nums2 = [1,3,2,1]
tuple = (nums, nums2)
# input: [1, 2, 1] output: [1, 2, 1, 1, 2, 1]
# input: [1, 3, 2, 1] output: [1, 3, 2, 1, 1, 3, 2, 1]
s = Solution()
for item in tuple:
    print("input:",item, "output:", s.getConcatenation(item))
