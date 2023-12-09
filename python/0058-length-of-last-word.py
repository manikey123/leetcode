class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
	one shortcut
	"""
	#	return len(s.split()[-1])
        c = 0
        for i in s[::-1]: # direct string usage
            if i == " ": # first occurance of space after the word, use that to exit
                if c >= 1:
                    return c
            else:
                c += 1
        return c
s = "Hello World"
s2 = "   fly me   to   the moon  "
s3 = "luffy is still joyboy"
tuple = (s , s2, s3)
for item in tuple:
    print("Input:",item, "Output:", Solution().lengthOfLastWord(item))