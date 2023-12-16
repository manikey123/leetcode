from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array in-place and returns the new length.

        Args:
        nums (List[int]): The sorted array from which duplicates are to be removed.

        Returns:
        int: The length of the array after removing duplicates.
        """
        if not nums:
            return 0  # Return 0 if the array is empty

        # Initialize a pointer for the position of the next unique element
        unique_pos = 0

        # Iterate over the array
        for i in range(1, len(nums)):
            # If the current element is different from the element at unique_pos
            if nums[i] != nums[unique_pos]:
                unique_pos += 1  # Increment unique_pos
                nums[unique_pos] = nums[i]  # Update the element at unique_pos

        # The length of the array without duplicates is unique_pos + 1
        return unique_pos + 1

# Test cases
def run_test_cases():
    solution = Solution()
    test_cases = [
        ([1,1,2], 2),  # Example 1
        ([0,0,1,1,1,2,2,3,3,4], 5),  # Example 2
        # Additional test cases
        ([], 0),  # Empty array
        ([1,2,3,4,5], 5),  # Array with no duplicates
        ([1,1,1,1,1], 1)  # Array with all duplicates
    ]

    for nums, expected in test_cases:
        result = solution.removeDuplicates(nums)
        assert result == expected, f"Test failed for nums: {nums}. Expected: {expected}, got: {result}"

    print("All test cases passed!")

run_test_cases()
