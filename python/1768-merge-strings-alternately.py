class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        res = []

        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        res.append(word1[i:])
        res.append(word2[j:])
        return ''.join(res)

nums  = "abc" ; target = "pqr"
nums2 = "ab"; target2 = "pqrs"
nums3 = "abcd" ; target3 = "pq"
tuple = (  (nums,target) , (nums2,target2) , (nums3,target3) )
# input1: ('abc', 'pqr') result: apbqcr
# input1: ('ab', 'pqrs') result: apbqrs
# input1: ('abcd', 'pq') result: apbqcd
for item in tuple:
    print("input1:",item, "result:", Solution().mergeAlternately(item[0], item[1]))