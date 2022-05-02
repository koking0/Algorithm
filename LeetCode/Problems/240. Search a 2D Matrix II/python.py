from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        row_index, col_index = 0, cols - 1
        while row_index < rows and col_index > -1:
            if matrix[row_index][col_index] < target:
                row_index += 1
            elif matrix[row_index][col_index] > target:
                col_index -= 1
            else:
                return True
        return False
