from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            # count += (1 if n == res else -1)
            if n == res:
                count += 1
            else:
                count -= 1
        return res




# def majorityElement(nums):
#     count_dict = {}
#
#     for num in nums:
#         if num in count_dict:
#             count_dict[num] += 1
#         else:
#             count_dict[num] = 1
#
#         # Check if the current element is the majority element
#         if count_dict[num] > len(nums) // 2:
#             return num
#
# # Example usage:
# nums1 = [3, 2, 3]
# nums2 = [2, 2, 1, 1, 1, 2, 2]
#
# result1 = majorityElement(nums1)
# result2 = majorityElement(nums2)
#
# print("Output:", result1)  # Output: 3
# print("Output:", result2)  # Output: 2
#
# ------------------------------------------------------------------------------------------
#
# def majorityElement(nums):
#     count_dict = {}
#
#     for num in nums:
#         count_dict[num] = count_dict.get(num, 0) + 1
#
#         # Check if the current element is the majority element
#         if count_dict[num] > len(nums) // 2:
#             return num
#
# # Example usage:
# nums1 = [3, 2, 3]
# nums2 = [2, 2, 1, 1, 1, 2, 2]
#
# result1 = majorityElement(nums1)
# result2 = majorityElement(nums2)
#
# print("Output:", result1)  # Output: 3
# print("Output:", result2)  # Output: 2




nums = [3,2,3]
nums2 = [2,2,1,1,1,2,2]
tuple = (nums , nums2)
# Input: [3, 2, 3] Output: 3
# Input: [2, 2, 1, 1, 1, 2, 2] Output: 2
for item in tuple:
    print("Input:",item, "Output:", Solution().majorityElement(item))