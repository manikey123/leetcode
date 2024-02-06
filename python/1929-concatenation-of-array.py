from typing import List

# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         return nums+nums
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for _ in range(2):  # Loop twice over the nums list
            for n in nums:  # Iterate through each element in nums
                ans.append(n)  # Append each element to the ans list
        return ans

    def getConcatenation2(self, nums: List[int]) -> List[int]:
        ans = []
        for _ in range(2):  # Loop twice
            ans.extend(nums)  # Extend 'ans' with 'nums' in each iteration
        return ans


nums = [1,2,1]
print("multiply by 2",nums*2)
nums2 = [1,3,2,1]
tuple = (nums, nums2)
# input: [1, 2, 1] output: [1, 2, 1, 1, 2, 1]
# input: [1, 3, 2, 1] output: [1, 3, 2, 1, 1, 3, 2, 1]
s = Solution()
for item in tuple:
    print("input:",item, "output using append:", s.getConcatenation(item))
for item in tuple:
    print("input:", item, "output using extend:", s.getConcatenation2(item))

