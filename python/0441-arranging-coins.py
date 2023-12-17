class Solution:
    def arrangeCoinsIterative(self, n: int) -> int:
        # Initialize row and coin count
        row, coins = 0, 0

        # Iterate until the coins run out
        while coins <= n:
            row += 1  # Move to the next row
            coins += row  # Add coins to the current row

        # The last row is incomplete, so return row - 1
        return row - 1

    def arrangeCoinsFormula(self, n: int) -> int:
        # Using the quadratic formula to solve k(k + 1)/2 = n
        return int(((-1 + (1 + 8 * n) ** 0.5) / 2))

# Test cases
sol = Solution()
assert sol.arrangeCoinsIterative(5) == 2  # Example 1
assert sol.arrangeCoinsIterative(8) == 3  # Example 2

assert sol.arrangeCoinsFormula(5) == 2  # Example 1
assert sol.arrangeCoinsFormula(8) == 3  # Example 2

# Additional Test Cases
assert sol.arrangeCoinsIterative(10) == 4
assert sol.arrangeCoinsFormula(10) == 4

'''
### Explanation of the Code
- `arrangeCoinsIterative` uses a loop to add coins to each row until the total number of coins exceeds `n`.
- `arrangeCoinsFormula` uses the quadratic formula to find the largest integer `k` such that \( \frac{k(k + 1)}{2} \leq n \).

### Time and Space Complexity
- **Iterative Approach**:
  - **Time Complexity**: O(√n), as the number of iterations is proportional to the square root of `n`.
  - **Space Complexity**: O(1), as it uses constant space.
- **Mathematical Approach**:
  - **Time Complexity**: O(1), as it involves a constant number of operations.
  - **Space Complexity**: O(1), as it uses constant space.
'''