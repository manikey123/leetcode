class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
        return r
s = 4
s2 = 8
tuple = (s , s2)
# Input: 4 Output: 2
# Input: 8 Output: 2
for item in tuple:
    print("Input:",item, "Output:", Solution().mySqrt(item))