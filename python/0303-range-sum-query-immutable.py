from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        cur = 0
        for n in nums:
            cur += n
            self.prefix.append(cur)
        
        
    def sumRange(self, left: int, right: int) -> int:
        r = self.prefix[right] 
        l = self.prefix[left - 1] if left > 0 else 0
        return r - l

s = [[-2, 0, 3, -5, 2, -1], [0, 2], [2, 5], [0, 5]]
# Input: ['flower', 'flow', 'flight'] Output: fl
# Input: ['dog', 'racecar', 'car'] Output:

n = NumArray(s[0])
for i in range(1,len(s)):
    input = s[i]
    print("Input:",  input , "Output:",n.sumRange(input[0], input[1]))