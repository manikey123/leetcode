# Time Complexity: O(m + n), we check each element of nums1Set and nums2Set
# Space Complexity: O(m + n), where m and n are length sets in worst case.

from typing import List  # ignore this, just for typing


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        # lst1 = [num for num in nums1_set if num not in nums2_set]
        # lst2 = [num for num in nums2_set if num not in nums1_set]
        # Initialize an empty list
        lst1 = []

        # Iterate through elements in nums1_set
        for num in nums1_set:
            # Check if the current element is not in nums2_set
            if num not in nums2_set:
                # Add the element to lst1
                lst1.append(num)

        # Initialize an empty list
        lst2 = []

        # Iterate through elements in nums2_set
        for num in nums2_set:
            # Check if the current element is not in nums1_set
            if num not in nums1_set:
                # Add the element to lst2
                lst2.append(num)
        return [lst1, lst2]
nums  = [1,2,3] ; target = [2,4,6]
nums2 = [1,2,3,3]; target2 = [1,1,2,2]
tuple = (  (nums,target) , (nums2,target2) )
# input1: ([1, 2, 3], [2, 4, 6]) result: [[1, 3], [4, 6]]
# input1: ([1, 2, 3, 3], [1, 1, 2, 2]) result: [[3], []]
for item in tuple:
    print("input1:",item, "result:", Solution().findDifference(item[0], item[1]))