from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res
prices  = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]
prices3 = [7,6,2,9,1,7]
tuple = (prices,prices2, prices3)
#Result:
# Input: [7, 1, 5, 3, 6, 4] Output: 5
# Input: [7, 6, 4, 3, 1] Output: 0
# Input: [7, 6, 2, 9, 1, 8] Output: 7

#
s = Solution()
for item in tuple:
    print("Input:",item, "Output:", s.maxProfit(item))
