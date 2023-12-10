from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_dict = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        for char in text:
            if char in balloon_dict:
                balloon_dict[char] += 1

        balloon_dict['l'] //= 2
        balloon_dict['o'] //= 2

        return min(balloon_dict.values())
s = "nlaebolko"
s2 = "loonbalxballpoon"
s3 = "leetcode"
tuple = (s , s2, s3)
# Input: nlaebolko Output: 1
# Input: loonbalxballpoon Output: 2
# Input: leetcode Output: 0
for item in tuple:
    print("Input:",item, "Output:", Solution().maxNumberOfBalloons(item))