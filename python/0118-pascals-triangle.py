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

        prev_rows = self.generateDP(numRows - 1)
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
            return self.generateDP(rowIndex - 1)

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

    def generate_iterative1(self, numRows):
        """
        Generate Pascal's triangle using an iterative approach.
        Time Complexity: O(numRows^2)
        Space Complexity: O(numRows^2)
        """
        if numRows == 0:
            return []

        triangle = [[1]]

        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
            triangle.append(row)
        return triangle


    def generatePascalsTriangleGG(self,numRows):
        if numRows == 0:  # If no rows, return an empty list
            return []

        triangle = [[1]]  # Initialize the triangle with the first row

        for row_num in range(1, numRows):  # Start from the second row
            row = [1]  # Every row starts with 1
            prev_row = triangle[row_num - 1]  # Get the previous row

            # Iterate through the previous row to calculate the values for the current row
            for j in range(1, len(prev_row)):
                # Sum the two adjacent values from the previous row
                row.append(prev_row[j - 1] + prev_row[j])

            row.append(1)  # Every row ends with 1
            triangle.append(row)  # Add the constructed row to the triangle

        return triangle
numRows = 5
numRows2 = 1
tuple = (numRows , numRows2)
# Input: 5 Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
# Input: 1 Output: [[1]]
for item in tuple:
    print("Input:",item, "generate:", Solution().generate(item))
    print("Input:",item, "generate_iterative1:", Solution().generatePascalsTriangleGG(item))