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

'''
3. **For Each Price in `prices1`**:
   - **Day 1**: Price = 7
     - `min_price` becomes `min(inf, 7)`, which is 7.
     - Profit if sold today = 7 - 7 = 0.
     - `max_profit` remains `max(0, 0)`, which is 0.
   - **Day 2**: Price = 1
     - `min_price` becomes `min(7, 1)`, which is 1.
     - Profit if sold today = 1 - 1 = 0.
     - `max_profit` remains `max(0, 0)`, which is 0.
   - **Day 3**: Price = 5
     - `min_price` is still 1.
     - Profit if sold today = 5 - 1 = 4.
     - `max_profit` becomes `max(0, 4)`, which is 4.
   - **Day 4**: Price = 3
     - `min_price` is still 1.
     - Profit if sold today = 3 - 1 = 2.
     - `max_profit` remains `max(4, 2)`, which is 4.
   - **Day 5**: Price = 6
     - `min_price` is still 1.
     - Profit if sold today = 6 - 1 = 5.
     - `max_profit` becomes `max(4, 5)`, which is 5.
   - **Day 6**: Price = 4
     - `min_price` is still 1.
     - Profit if sold today = 4 - 1 = 3.
     - `max_profit` remains `max(5, 3)`, which is 5.

4. **Result**:
   - After iterating through all the prices, the `max_profit` is found to be 5. This is the maximum profit that can be achieved with the given prices, by buying at the price of 1 and selling at the price of 6. 

The function then returns this `max_profit` value, which in this case is 5.
'''