from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # O (n + m)
        # nums1Idx = { n:i for i, n in enumerate(nums1) }
        # nums1Idx = dict(enumerate(nums1))

        # nums1Idx = {}
        # # nums1Idx = {n: i for i, n in enumerate(nums1)}
        # for i , n in enumerate(nums1):
        #     nums1Idx[n] = i
        #
        #
        # res = [-1] * len(nums1)
        #
        # stack = []
        # for   no  in nums2:
        #
        #
        #     # while stack exists and current is greater than the top of the stack
        #     while stack and no > stack[-1]: #while loop that continues as long as the stack is not empty (stack) and the current element cur is greater than the top element of the stack (stack[-1]).
        #         val = stack.pop() # take top val
        #         idx = nums1Idx[val]
        #         res[idx] = no
        #
        #     if no in nums1Idx:
        #         stack.append(no)
        #
        # return res
    
    
        # O (n * m)
        nums1Idx = { n:i for i, n in enumerate(nums1) }
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    res[idx] = nums2[j]
                    break

        return res
#
# input1: ([4, 1, 2], [1, 3, 4, 2]) result: [-1, 3, -1]
# input1: ([2, 4], [1, 2, 3, 4]) result: [3, -1]


nums1 = [4,1,2] ;  nums11 = [1,3,4,2]
nums2 = [2, 4]; nums22 = [1, 2, 3, 4]

tuple = (  (nums1,nums11) , (nums2,nums22)  )
for item in tuple:
    print("input1:",item, "result:", Solution().nextGreaterElement(item[0], item[1]))
