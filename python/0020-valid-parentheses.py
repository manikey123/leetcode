from typing import List

class Solution:
    def isValid2(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []
        # Hash map for keeping track of mappings. This provides a fast lookup for the closing brackets
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression
        for ch in s:
            # If the chacter is a closing bracket
            if ch in mapping:
                # Pop the topmost element from the stack, if it is non-empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                # top_element = stack.pop() if stack else '#'

                if not stack:
                    return False  # Stack #if u get directly closed bracker then direct exit pip
                top_element = stack.pop()
                # The mapping for the opening bracket in our hash and the top element of the stack don't match, return false
                if mapping[ch] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack
                stack.append(ch)

        # If the stack is empty, return true. Otherwise, return false
        return not stack

    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets

        stack = []
        # Hash map for keeping track of mappings. This maps opening brackets to their corresponding closing brackets
        mapping = {"(": ")", "{": "}", "[": "]"}

        # For every bracket in the expression
        for ch in s:
            # If the chacter is an opening bracket
            if ch in mapping:
                # Push the corresponding closing bracket onto the stack
                stack.append(mapping[ch])
            else:
                # If the stack is empty or the chacter does not match the top element of the stack, return false
                if not stack or ch != stack.pop():
                    return False

        # If the stack is empty, return true. Otherwise, return false
        return not stack #return true when nothing in stack

# Test Cases
sol = Solution()
assert sol.isValid("()") == True  # Example 1
assert sol.isValid("()[]{}") == True  # Example 2
assert sol.isValid("(]") == False  # Example 3

# Additional Test Cases
assert sol.isValid("{[]}") == True
assert sol.isValid("([)]") == False
assert sol.isValid("") == True  # Empty string
print("completed successfully congrats")
