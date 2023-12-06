import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
list1 = ["eat","tea","tan","ate","nat","bat"]
list2 = ["a"]
list = [ list1, list2]

s = Solution()
for item in list:
    print( s.groupAnagrams(item))
