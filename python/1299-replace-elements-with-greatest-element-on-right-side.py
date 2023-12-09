from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        for i in range(len(arr) -1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
            print("test")
        return arr
# arr2 = [400]
arr = [17,18,5,4,6,1]

# input item [17, 18, 5, 4, 6, 1]
# output: [18, 6, 6, 6, 1, -1]
# input item [400]
# output: [-1]
tuple2 = [  arr  ]
for item in tuple2:
    print("input item", item )
    print("output:", Solution().replaceElements(item))
