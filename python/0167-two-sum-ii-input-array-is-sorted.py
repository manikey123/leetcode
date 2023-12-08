from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
nums  = [2,7,11,15] ; target = 9
nums2 = [2,3,4]; target2 = 6
nums3 = [-1,0] ; target3 = -1

tuple = (  (nums,target) , (nums2,target2) , (nums3,target3) )
s = Solution()
for item in tuple:
    print("input:",item, "result:", s.twoSum(item[0], item[1]))
