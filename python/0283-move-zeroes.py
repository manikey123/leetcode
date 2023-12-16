from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize a pointer for the position of the next non-zero element
        non_zero_index = 0

        # Iterate over the array
        for i in range(len(nums)):
            # If the current element is non-zero
            if nums[i] != 0:
                # Swap the current element with the element at the non-zero index
                nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
                # Increment the non-zero index
                non_zero_index += 1

# Test cases from the problem
sol = Solution()

# Example 1
nums1 = [0, 1, 0, 3, 12]
sol.moveZeroes(nums1)
print("Example 1 Result:", nums1)  # Expected Output: [1, 3, 12, 0, 0]

# Example 2
nums2 = [0]
sol.moveZeroes(nums2)
print("Example 2 Result:", nums2)  # Expected Output: [0]

# Additional Test Cases
# Test case with multiple zeros
nums3 = [0, 0, 1, 0, 3, 12]
sol.moveZeroes(nums3)
print("Additional Test Case 1 Result:", nums3)  # Expected Output: [1, 3, 12, 0, 0, 0]

# Test case with no zeros
nums4 = [1, 2, 3, 4]
sol.moveZeroes(nums4)
print("Additional Test Case 2 Result:", nums4)  # Expected Output: [1, 2, 3, 4]

# Test case with all zeros
nums5 = [0, 0, 0, 0]
sol.moveZeroes(nums5)
print("Additional Test Case 3 Result:", nums5)  # Expected Output: [0, 0, 0, 0]
