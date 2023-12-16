from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Find the maximum profit that can be achieved from buying and selling a stock.
        """
        # Initialize minimum price and maximum profit
        min_price = float('inf')
        max_profit = 0

        # Iterate over the prices
        for price in prices:
            # Update the minimum price if the current price is lower
            min_price = min(min_price, price)
            # Calculate the profit if the stock is sold today
            profit = price - min_price
            # Update the maximum profit if the current profit is higher
            max_profit = max(max_profit, profit)

        return max_profit

# Test cases from the problem
sol = Solution()

# Example 1
prices1 = [7,1,5,3,6,4]
print("Example 1 Result:", sol.maxProfit(prices1))  # Expected Output: 5

# Example 2
prices2 = [7,6,4,3,1]
print("Example 2 Result:", sol.maxProfit(prices2))  # Expected Output: 0

# Additional Test Cases
# Test case with increasing prices
prices3 = [1, 2, 3, 4, 5]
print("Additional Test Case 1 Result:", sol.maxProfit(prices3))  # Expected Output: 4

# Test case with fluctuating prices
prices4 = [3, 2, 6, 5, 0, 3]
print("Additional Test Case 2 Result:", sol.maxProfit(prices4))  # Expected Output: 4

# Test case with constant prices
prices5 = [5, 5, 5, 5, 5]
print("Additional Test Case 3 Result:", sol.maxProfit(prices5))  # Expected Output: 0
