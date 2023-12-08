def guess(mid):
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        # return a num btw 1,..,n
        
        low = 1
        high = n
        
        while True:
            mid = low + (high - low) // 2
            myGuess = guess(mid)
            if myGuess == 1:
                low = mid + 1
            elif myGuess == -1:
                high = mid - 1
            else:
                return mid
nums  = 10 ; target = 6
nums2 = 1; target2 = 1
nums3 = 2 ; target3 = 1
tuple = (  (nums,target) , (nums2,target2) , (nums3,target3) )
for item in tuple:
    print("input1:",item, "result:", Solution().guessNumber(item[0]))