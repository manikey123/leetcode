class Solution:


## Why sliding window and not hashMap ??
## As we need to ensure the sequnece of the characters
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        #ensure j is used for the target string t
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1 # i is guarding s
            j += 1   # j is guarding t
        return i == len(s)
s  =  "abc" ; t = "ahbgdc"
s2 = "axc"; t2 = "ahbgdc"
nums3 = [3,3] ; target3 = 6
tuple = (  (s,t) , (s2,t2) )
# input1: ('abc', 'ahbgdc') result: True
# input1: ('axc', 'ahbgdc') result: False
for item in tuple:
    print("input1:",item, "result:", Solution().isSubsequence(item[0], item[1]))
