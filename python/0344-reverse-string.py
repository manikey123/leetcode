from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while l < r:
            s[l],s[r] = s[r],s[l]
            l += 1
            r -= 1
s = ["h","e","l","l","o"]
s2 = ["H","a","n","n","a","h"]
tuple = (s , s2)
# Input: ['o', 'l', 'l', 'e', 'h'] Output: None
# Input: ['h', 'a', 'n', 'n', 'a', 'H'] Output: None
for item in tuple:
    print("Input:",item, "Output:", Solution().reverseString(item))