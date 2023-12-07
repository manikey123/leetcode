from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

nums  = [2,7,11,15] ; target = 3; numss= [2,7,11,15] ; targets = 9
nums2 = [3,2,4]; target2 = 6; nums22 = [3,2,4]; target22 = 6
nums3 = [3,3] ; target3 = 6; nums33 = [3,3] ; target33 = 6
tuple = ((nums,target, numss,targets) , (nums2,target2,nums22,target22 ) , (nums3,target3,nums33,target33 ) )
for item in tuple:
    print("input1:",item, "result:", Solution().merge(item[0], item[1] , item[2], item[3]))