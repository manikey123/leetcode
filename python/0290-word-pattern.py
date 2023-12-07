class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        charToWord = {}
        wordToChar = {}
        
        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w
            wordToChar[w] = c
        return True
nums  = "abba" ; target = "dog cat cat dog"
nums2  = "abba" ; target2 = "dog cat cat fish"
nums3 = "aaaa" ; target3 = "dog cat cat dog"
tuple = (  (nums,target) , (nums2,target2) , (nums3,target3) )
# input1: ('abba', 'dog cat cat dog') result: True
# input1: ('abba', 'dog cat cat fish') result: False
# input1: ('aaaa', 'dog cat cat dog') result: False
for item in tuple:
    print("input1:",item, "result:", Solution().wordPattern(item[0], item[1]))
