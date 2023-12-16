from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges two sorted arrays nums1 and nums2 into a single sorted array in-place.
        Args:
        nums1 (List[int]): The first sorted array with m meaningful elements followed by enough space to accommodate nums2.
        m (int): The number of meaningful elements in nums1.
        nums2 (List[int]): The second sorted array.
        n (int): The number of elements in nums2.
        """

        # Start from the end of nums1 and nums2
        p1, p2, i = m - 1, n - 1, m + n - 1

        # Iterate while there are elements in nums2
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
            i -= 1

# Example usage and test cases
sol = Solution()

# Test Case 1 from LeetCode
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
sol.merge(nums1, m, nums2, n)
print(nums1)  # Expected output: [1,2,2,3,5,6]

# Test Case 2 from LeetCode
nums1 = [1]
m = 1
nums2 = []
n = 0
sol.merge(nums1, m, nums2, n)
print(nums1)  # Expected output: [1]

# Test Case 3 from LeetCode
nums1 = [0]
m = 0
nums2 = [1]
n = 1
sol.merge(nums1, m, nums2, n)
print(nums1)  # Expected output: [1]

# Additional Test Cases
additional_cases = [
    ([4,0,0,0,0,0], 1, [1,2,3,5,6], 5, [1,2,3,4,5,6]),
    ([10,0,0,0], 1, [2,5,6], 3, [2,5,6,10]),
     # ([], 0, [1], 1, [1]),
    # ([1,2,3,0,0,0], 3, [], 0, [1,2,3])
]

for nums1, m, nums2, n, expected in additional_cases:
    sol.merge(nums1, m, nums2, n)
    assert nums1 == expected, f"Test failed for nums1: {nums1}, nums2: {nums2}"
    print(f"Test passed for nums1: {nums1}, nums2: {nums2}")
