class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for c1, c2 in zip(s, t):
            if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1

        return True

s  = "egg" ; target = "add"
s2 = "foo"; target2 = "bar"
s3 = "paper" ; target3 = "title"
tuple = (  (s,target) , (s2,target2) , (s3,target3) )
# input1: ('egg', 'add') result: True
# input1: ('foo', 'bar') result: False
# input1: ('paper', 'title') result: True
for item in tuple:
    print("input1:",item, "result:", Solution().isIsomorphic(item[0], item[1]))