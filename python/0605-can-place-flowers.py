from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Solution with O(1) space complexity
        empty = 0 if flowerbed[0] else 1

        for f in flowerbed:
           if f:
               n -= int((empty - 1) / 2)  # int division, round toward zero
               empty = 0
           else:
               empty += 1

        n -= (empty) // 2
        return n <= 0
        
class Solution2:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
       # Another solution with O(1) space complexity
       for i in range(len(flowerbed)):
            if n == 0:
                return True
            # ensure the ends are coered with 0 check first and then the normal condition
            if ((i == 0 or flowerbed[i - 1] == 0)   # If at the first element or the previous element equals to 0
                and (flowerbed[i] == 0)             # If current element equals to 0
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)): # If at the last element or the next element equals to 0
                # Place flower at the current position
                flowerbed[i] = 1
                n -= 1

       return n == 0
       
class Solution3:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
       # Solution with O(n) space complexity
       f = [0] + flowerbed + [0]
       # by embedding the ends with 0 we remoe the zero at the ends of the code
       
       for i in range(1, len(f) - 1):  # skip first & last
           if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
               f[i] = 1
               n -= 1
       return n <= 0


nums  = [1,0,0,0,1] ; target = 1
nums2 = [1,0,0,0,1]; target2 = 2
tuple = (  (nums,target) , (nums2,target2)  )
# input1: ([1, 0, 0, 0, 1], 1) result: True
# input1: ([1, 0, 0, 0, 1], 2) result: False
for item in tuple:
    print("input1:",item, "result:", Solution().canPlaceFlowers(item[0], item[1]))
    print("input1:",item, "result:", Solution2().canPlaceFlowers(item[0], item[1]))
    print("input1:",item, "result:", Solution3().canPlaceFlowers(item[0], item[1]))