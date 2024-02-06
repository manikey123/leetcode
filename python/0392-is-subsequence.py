class Solution:


## Why sliding window and not hashMap ??
## As we need to ensure the sequnece of the characters
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        #ensure j is used for the target string t
        while i < len(s) and j < len(t): #running both strings parallely
            print(s[i], t[j])
            if s[i] == t[j]: #matching condition
                i += 1 # when there is character match beteen first and second string increment i pointer ie slow++
            j += 1   # j pointer keeps incrementing for the second larger string

        return i == len(s)

    def isSubsequenceFor(self, s, t):
        s_index = 0  # Initialize index for s
        s_len = len(s)  # Length of s to avoid multiple len() calls

        # Iterate over each character in t using a for loop
        for char in t:
            # Check if we have already found all characters of s
            if s_index == s_len:
                break  # All characters in s are found, exit the loop

            # If the current character in t matches the current character in s
            if s[s_index] == char:
                s_index += 1  # Move to the next character in s

        # Check if all characters in s were found in t
        return s_index == s_len


s  =  "abc" ; t = "ahbgdc"
s2 = "axc"; t2 = "ahbgdc"
nums3 = [3,3] ; target3 = 6
tuple = (  (s,t) , (s2,t2) )
# input1: ('abc', 'ahbgdc') result: True
# input1: ('axc', 'ahbgdc') result: False
for item in tuple:
    print("input1:",item, "result:", Solution().isSubsequence(item[0], item[1]))

for item in tuple:
    print("input1:",item, "result:", Solution().isSubsequenceFor(item[0], item[1]))






