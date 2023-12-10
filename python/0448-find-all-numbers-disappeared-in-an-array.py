from typing import List

# In this code, the first loop iterates through the array nums and uses the abs() function to get the absolute value of each element. It then uses this value as an index to mark the corresponding position in the array by making the element negative.
# The second loop iterates through the modified array, and for each positive element, it means that the corresponding index (plus one) is missing in the original array, so it appends that index to the list of missing_numbers.
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for no in nums:
            i = abs(no) - 1 #nums have values from 1 to 8 while index is from 0 to 7
            nums[i] = -1 * abs(nums[i]) #marks the corresponding position in the array by making the element negative. This helps identify whether a number has been encountered or not. The abs() function is used to ensure that the value is positive.

        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res

    def findDisappearedNumbersSet(nums):
        n = len(nums)
        num_set = set(nums)

        missing_numbers = []

        for i in range(1, n + 1):
            if i not in num_set:
                missing_numbers.append(i)

        return missing_numbers

    # Example usage:
    nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
    nums2 = [1, 1]

    result1 = findDisappearedNumbers(nums1)
    result2 = findDisappearedNumbers(nums2)

s = [4,3,2,7,8,2,3,1]
s2 = [1,1]
tuple = (s , s2)
# Input: [-4, -3, -2, -7, 8, 2, -3, -1] Output: [5, 6]
# Input: [-1, 1] Output: [2]
for item in tuple:
    print("Input:",item, "Output:", Solution().findDisappearedNumbers(item))