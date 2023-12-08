class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )
s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3= " "

tuple = (s1,s2,s3)
# Input: A man, a plan, a canal: Panama Output: True
# Input: race a car Output: False
# Input:   Output: True

#
s = Solution()
for item in tuple:
    print("Input:",item, "Output:", s.isPalindrome(item))