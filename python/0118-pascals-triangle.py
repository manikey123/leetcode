from typing import List


class Solution:
    #https://leetcode.com/problems/pascals-triangle/solutions/4016203/three-approaches-beginner-friendly-full-explanation-c-java-python/

    def generateRS(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        prevRows = self.generate(numRows - 1)
        newRow = [1] * numRows
        # index 1
        for i in range(1, numRows - 1):

            newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]

        prevRows.append(newRow)
        return prevRows

#     Combinatorial Formula Approach:
# Use the binomial coefficient formula C(n, k) to calculate each element.
# Build the triangle row by row using the formula.
    def generateCB(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 0:
            return result

        first_row = [1]
        result.append(first_row)

        for i in range(1, numRows):
            prev_row = result[i - 1] #as it ascending
            current_row = [1]

            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])

            current_row.append(1)
            result.append(current_row)

        return result

    def generateDP(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        prev_rows = self.generate(numRows - 1)
        prev_row = prev_rows[-1]
        current_row = [1]

        for i in range(1, numRows - 1):
            current_row.append(prev_row[i - 1] + prev_row[i])

        current_row.append(1)
        prev_rows.append(current_row)

        return prev_rows




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
