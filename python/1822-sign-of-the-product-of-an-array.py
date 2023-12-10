from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # Initialize a flag as True
        flag = True

        # Iterate through the elements in nums
        for i in nums:
            # If the current element is 0, return 0 (product will be 0)
            if i == 0:
                return 0
            # If the current element is negative, toggle the flag
            if i < 0:
                flag = not flag

        # If the flag is True, return 1; otherwise, return -1
        if flag:
            return 1
        else:
            return -1
        # return 1 if flag else -1

    def arraySign(self, nums: List[int]) -> int:
        # Initialize a flag as True
        flag = True

        # Check if there is any zero in nums, if yes, return 0
        if 0 in nums:
            return 0

        # Determine the sign by checking if the count of negative numbers is even or odd
        return 1 if len([num for num in nums if num < 0]) % 2 == 0 else -1


# Test cases
s = [-1, -2, -3, -4, 3, 2, 1]
s2 = [1, 5, 0, 2, -3]
s3 = [-1, 1, -1, 1, -1]
tuple = (s, s2, s3)

# Print results for test cases
for item in tuple:
    print("Input:", item, "Output:", Solution().arraySign(item))