from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []

        for op in ops:
            if op == '+':
                # Add the sum of the last two scores
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                # Double the last score
                stack.append(2 * stack[-1])
            elif op == 'C':
                # Remove the last score
                stack.pop()
            else:
                # Add the score as an integer
                stack.append(int(op))

        # Sum up all the scores
        return sum(stack)

# Test cases from LeetCode
solution = Solution()
assert solution.calPoints(["5","2","C","D","+"]) == 30
assert solution.calPoints(["5","-2","4","C","D","9","+","+"]) == 27
assert solution.calPoints(["1","C"]) == 0

# Additional test cases
assert solution.calPoints(["10","20","D","+","C"]) == 40
assert solution.calPoints(["3","D","C","+","5"]) == 11
