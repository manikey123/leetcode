from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        score_stack = []
        
        for o in operations:
            
            # it is +, D, or C
            # if stack isn't of sufficient length, then operation is voided
            if o == "+" and len(score_stack) >= 2:
                summed = score_stack[-2] + score_stack[-1]
                score_stack.append(summed)
                
            elif o == "D" and len(score_stack) >= 1:
                doubled = score_stack[-1] * 2
                score_stack.append(doubled)
                
            elif o == "C" and len(score_stack) >= 1:
                score_stack.pop() 
                
            else: 
                score_stack.append(int(o))

        return sum(score_stack)

s = ["5","2","C","D","+"]
s2 = ["5","-2","4","C","D","9","+","+"]
s3 = ["1","C"]
tuple = (s , s2, s3)
# Input: ['5', '2', 'C', 'D', '+'] Output: 30
# Input: ['5', '-2', '4', 'C', 'D', '9', '+', '+'] Output: 27
# Input: ['1', 'C'] Output: 0
for item in tuple:
    print("Input:",item, "Output:", Solution().calPoints(item))