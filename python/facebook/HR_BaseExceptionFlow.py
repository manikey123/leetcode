import math
import os
import random
import re
import sys


def multiply(a, b, bound):
    # write your code here

    result = a * b
    if result > bound:
        raise ValueError("multiplication of " + str(a) + " and " + str(b) + " with bound")
    return result

print(multiply(2,5,20))
print(multiply(2,5,8))
p



# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     q = int(input())
#     for _ in range(q):
#         a, b, bound = map(int, input().split())
#         try:
#             res = multiply(a, b, bound)
#             fptr.write("%d\n" % res)
#         except ValueError as e:
#             fptr.write("%s\n" % e)
#     fptr.close()