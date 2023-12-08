class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.validPalindromeUtil(s, i + 1, j) or self.validPalindromeUtil(s, i, j - 1)
        return True
    
    def validPalindromeUtil(self, s, i, j):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True
s = "aba"
s2 = "abca"
s3 = "abc"
tuple = (s , s2, s3)
# Input: aba Output: True
# Input: abca Output: True
# Input: abc Output: False
for item in tuple:
    print("Input:",item, "Output:", Solution().validPalindrome(item))
