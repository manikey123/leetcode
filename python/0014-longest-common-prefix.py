from typing import List


class Solution:
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        res = ""  # Initialize the result string, which will store the longest common prefix
        lengthofFirstString = len(strs[0])  # Get the length of the first string in the list

        # Iterate over each character index of the first string
        for i in range(lengthofFirstString):
            # Iterate over the remaining strings in the list starting from the second string
            for ch in strs[1:]:
                # Check two conditions for each string ch in the list:
                # 1. If the current index i is equal to the length of the string ch, it means we've reached the end of ch
                # 2. If the character at index i in string ch is not the same as the character at index i in the first string
                if i == len(ch) or ch[i] != strs[0][i]:
                    # If either condition is true, we've found the end of the common prefix
                    # Print the current state for debugging and return the result accumulated so far
                    print("test", strs, res)
                    return res

            # If the current character at index i is common to all strings checked so far, append it to the result
            res += strs[0][i]

        # After checking all characters in the first string, return the accumulated result
        return res
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

    def longestCommonPrefix3(strs):
        if not strs:
            return ""

        # Start with the first string in the list as the prefix
        prefix = strs[0]

        # Compare the prefix with each string in the list
        for s in strs[1:]:
            # While the current string does not start with the prefix
            while not s.startswith(prefix):
                # Shorten the prefix by one character from the end
                prefix = prefix[:-1]
                # If the prefix becomes empty, no common prefix exists
                if not prefix:
                    return ""

        # Return the common prefix after checking all strings
        return prefix

# s = ["flower","flow","flight"]
s = ["flower","flow","flight"]
s2 = ["dog","racecar","car"]
s3= ["baad", "chaax"]
s4 = ["cardboard", "cart", "carrot", "carbon"]
tuple = (s , s2, s3, s4)
# Input: ['flower', 'flow', 'flight'] Output: fl
# Input: ['dog', 'racecar', 'car'] Output:
for item in tuple:
    print("Input:",item, "Output:", Solution().longestCommonPrefix3(item))
