class Solution:

    def isAnagram3(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm ={}

        for ch in s:
            hm[ch] = 1 + hm.get(ch, 0)
        for ch in t:
            if  (ch not in  hm.keys()) or hm[ch]==0:
                return False
            else :
                hm[ch] =hm[ch] -1
        return True
    
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm ={}

        for i in range(len(s)):
            hm[s[i]] = 1 + hm.get(s[i], 0)
        for i in range(len(t)):
            if  (t[i] not in  hm.keys()) or hm[t[i]]==0:
                return False
            else :
                hm[t[i]] =hm[t[i]] -1
        return True
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

s = Solution()

s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s,t))

s = "rat"
t = "car"
print(Solution().isAnagram(s,t))

#RES
# True
# False