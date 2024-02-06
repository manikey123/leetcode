class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
	one shortcut
	"""
	#	return len(s.split()[-1])
        c = 0
        for ch in s[::-1]: # direct string usage

            if ch  == " ": # first occurance of space after the word, use that to exit
                if c >= 1:
                    return c # exits the if loop , handles condition for multiple occurances of spaces
            else:
                c += 1
        return c
s = "Hello World"
s2 = "   fly me   to   the moon  "
s3 = "luffy is still joyboy"
tuple = ( s, s2, s3 )
# Input:    fly me   to   the moon   -->Res: 4
# Input: Hello World -->Res: 5
# Input: luffy is still joyboy -->Res: 6
for item in tuple:
    print("Input:",item, "-->Res:", Solution().lengthOfLastWord(item))