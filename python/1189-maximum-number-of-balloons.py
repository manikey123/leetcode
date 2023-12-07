from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        balloon = Counter("balloon")

        res = len(text)  # or float("inf")
        for c in balloon:
            res = min(res, countText[c] // balloon[c])
        return res
s = "nlaebolko"
s2 = "loonbalxballpoon"
s3 = "leetcode"
tuple = (s , s2, s3)
# Input: nlaebolko Output: 1
# Input: loonbalxballpoon Output: 2
# Input: leetcode Output: 0
for item in tuple:
    print("Input:",item, "Output:", Solution().maxNumberOfBalloons(item))