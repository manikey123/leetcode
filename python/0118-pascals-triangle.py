from typing import List


class Solution:
    def generate(self, rowIndex) -> List[List[int]]:
        if rowIndex == 0:
            return [[1]]
        else:
            return self.getAllRow(rowIndex - 1)

    def getAllRow(self, rowIndex):
        if rowIndex == 0:
            return [[1]]
        ListPrec = self.getAllRow(rowIndex - 1)
        Len = len(ListPrec[-1])
        ListPrec.append([1])
        for i in range(0, Len - 1):
            ListPrec[-1].append(ListPrec[-2][i] + ListPrec[-2][i + 1])
        ListPrec[-1].append(1)
        return ListPrec
numRows = 5
numRows2 = 1
tuple = (numRows , numRows2)
# Input: 5 Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
# Input: 1 Output: [[1]]
for item in tuple:
    print("Input:",item, "Output:", Solution().generate(item))