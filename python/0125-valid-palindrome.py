class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize left and right pointers for the two ends of the string
        l, r = 0, len(s) - 1

        # Continue comparing characters until the pointers meet
        while l < r:
            # Move left pointer to the next alphanumeric character
            while l < r and not self.alphanum(s[l]):  #handle spaces
                l += 1 #increase left only

            # Move right pointer to the next alphanumeric character
            while l < r and not self.alphanum(s[r]): #handle spaces
                r -= 1  #decrease right

            # Compare the characters (case-insensitive) at the current pointers
            if s[l].lower() != s[r].lower():
                return False

            # Move the pointers towards each other
            l += 1
            r -= 1

        # If the loop completes, the string is a palindrome
        return True

    # Helper function to check if a character is alphanumeric
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )

# Test cases
s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "

tuple = (s1, s2, s3)

# Input: A man, a plan, a canal: Panama Output: True
# Input: race a car Output: False
# Input:   Output: True
# Print results for test cases
s = Solution()
for item in tuple:
    print("Input:", item, "Output:", s.isPalindrome(item))
