class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Check if needle is an empty string
        if needle == "":
            return 0

        # Initialize the Longest Prefix Suffix (LPS) array with zeros
        lps = [0] * len(needle)

        # Calculate the LPS array using the Knuth-Morris-Pratt (KMP) algorithm
        prevLPS, i = 0, 1
        while i < len(needle):
            # If characters match, update LPS, increment pointers
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            # If characters don't match and no previous match, update LPS, increment pointer
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            # If characters don't match, move to the previous matching position in LPS
            else:
                prevLPS = lps[prevLPS - 1]

        # Pointers for haystack and needle
        i = 0  # Pointer for haystack
        j = 0  # Pointer for needle

        # Match the needle in the haystack
        while i < len(haystack):
            # If characters match, increment both pointers
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                # If no previous match, move to the next character in haystack
                if j == 0:
                    i += 1
                # If there is a previous match, move to the previous matching position in LPS
                else:
                    j = lps[j - 1]

            # If entire needle is matched, return the starting index in haystack
            if j == len(needle):
                return i - len(needle)

        # If no match is found, return -1
        return -1

# Test cases
nums = "sadbutsad"
target = "sad"
nums2 = "leetcode"
target2 = "leeto"
tuple = ((nums, target), (nums2, target2))

# Print results for test cases
for item in tuple:
    print("input1:", item, "result:", Solution().strStr(item[0], item[1]))
