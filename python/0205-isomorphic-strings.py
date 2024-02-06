class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Initialize two dictionaries to map characters from s to t and vice versa
        mapST, mapTS = {}, {}

        # Iterate over the characters of the strings
        for i in range(min(len(s), len(t))):
            # Extract corresponding characters from s and t
            c1, c2 = s[i], t[i]

            # Check if the current mapping violates the isomorphism
            # If c1 is already mapped to a different character, or
            # if c2 is already mapped to a different character, return False
            if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
                return False

            # Update the mappings
            mapST[c1] = c2
            mapTS[c2] = c1

        # If no violations were found, the strings are isomorphic
        return True

s  = "egg" ; target = "add"
s2 = "foo"; target2 = "bar"
s3 = "paper" ; target3 = "title"
tuple = (  (s,target) , (s2,target2) , (s3,target3) )
for item in tuple:
    print("input1:",item, "result:", Solution().isIsomorphic(item[0], item[1]))


