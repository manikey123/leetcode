class Solution:
    # def wordPattern(self, pattern: str, s: str) -> bool:
    #     words = s.split(" ")
    #     if len(pattern) != len(words):
    #         return False
    #     charToWord = {}
    #     wordToChar = {}
    #
    #     for c, w in zip(pattern, words):
    #         if c in charToWord and charToWord[c] != w:
    #             return False
    #         if w in wordToChar and wordToChar[w] != c:
    #             return False
    #         charToWord[c] = w
    #         wordToChar[w] = c
    #     return True

    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        # Using range and indexing to iterate through indices
        for i in range(len(pattern)):
            c, w = pattern[i], words[i]

            if c in char_to_word and char_to_word[c] != w:
                return False

            if w in word_to_char and word_to_char[w] != c:
                return False

            char_to_word[c] = w
            word_to_char[w] = c

        return True

    # Examples
    # print(wordPattern("abba", "dog cat cat dog"))  # Output: True
    # print(wordPattern("abba", "dog cat cat fish"))  # Output: False
    # print(wordPattern("aaaa", "dog cat cat dog"))  # Output: False


nums  = "abba" ; target = "dog cat cat dog"
nums2  = "abba" ; target2 = "dog cat cat fish"
nums3 = "aaaa" ; target3 = "dog cat cat dog"
tuple = (  (nums,target) , (nums2,target2) , (nums3,target3) )
# input1: ('abba', 'dog cat cat dog') result: True
# input1: ('abba', 'dog cat cat fish') result: False
# input1: ('aaaa', 'dog cat cat dog') result: False
for item in tuple:
    print("input1:",item, "result:", Solution().wordPattern(item[0], item[1]))
