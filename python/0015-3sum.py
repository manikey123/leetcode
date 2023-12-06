from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res

nums  = [-1,0,1,2,-1,-4]
nums2 = [0,1,1]
nums3 = [0,0,0]
tuple = (  (nums) , (nums2) , (nums3) )

s = Solution()
for item in tuple:
    print("input:",item, "output:", s.threeSum(item))

#Results:
# input: [-4, -1, -1, 0, 1, 2] output: [[-1, -1, 2], [-1, 0, 1]]
# input: [0, 1, 1] output: []
# input: [0, 0, 0] output: [[0, 0, 0]]