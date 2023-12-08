class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0
        while l <=r:
            mid = (l+r)//2
            coins = (mid /2) * (mid+1)
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(mid, res)
        return res
s = 5
s2 = 8
tuple = (s , s2)
# Input: 5 Output: 2
# Input: 8 Output: 3
for item in tuple:
    print("Input:",item, "Output:", Solution().arrangeCoins(item))