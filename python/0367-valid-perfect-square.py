class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num+1):
            if i * i == num:
                return True
            if i* i > num:
                return False
    
    
    
    def isPerfectSquare_2(self, num: int) -> bool:
        l ,r = 1, num
        while l <= r:
            mid = (l +r) // 2
            if mid * mid > num:
                r = mid - 1
            elif mid * mid < num:
                l = mid + 1
            else:
                return True
        return False

s = 16
s2 = 14
tuple = (s , s2)
# Input: 16 Output: True
# Input: 14 Output: False
for item in tuple:
    print("Input:",item, "Output:", Solution().isPerfectSquare(item))