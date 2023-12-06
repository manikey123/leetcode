from typing import List


class Solution:
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
    print("Input:",item, "Output:", Solution().longestCommonPrefix(item))