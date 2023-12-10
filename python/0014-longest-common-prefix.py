from typing import List


class Solution:
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        res = ""
        lengthofFirstString = len(strs[0])
        for i in range(lengthofFirstString):
        # check the for ch in the first word with every word until one word ends
            for ch in strs[1:]:  # itnerate the word of the string flow, flight
                #strs =["ab", "a"]
                # going through each str in list
                #end of string.under consideration     #avoid the first letters
                if i == len(ch)  or ch[i] != strs[0][i]: #i == len(ch) --> string ending ; # compare the ch or remaining strings with the first word corresponding component
                    print("test",s, res)
                    return res
            print(res)
            res += strs[0][i]
        return res
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

s = ["flower","flow","flight"]
s2 = ["dog","racecar","car"]
tuple = (s , s2)
# Input: ['flower', 'flow', 'flight'] Output: fl
# Input: ['dog', 'racecar', 'car'] Output:
for item in tuple:
    print("Input:",item, "Output:", Solution().longestCommonPrefix2(item))
