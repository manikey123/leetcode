class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
s = "()"
s2 = "()[]{}"
s3 ="(]"
tuple = (s , s2, s3)
# Input: () Output: True
# Input: ()[]{} Output: True
# Input: (] Output: False
for item in tuple:
    print("Input:",item, "Output:", Solution().isValid(item))