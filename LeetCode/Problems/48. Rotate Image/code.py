from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 当前旋转边的左上角和右下角
        leftTopRow, leftTopCol, rightDownRow, rightDownCol = 0, 0, len(matrix) - 1, len(matrix[-1]) - 1
        while leftTopRow <= rightDownRow and leftTopCol < rightDownRow:
            # 按照对应规则逐步旋转
            for i in range(rightDownCol - leftTopCol):
                matrix[leftTopRow][leftTopCol + i], matrix[leftTopRow + i][rightDownCol], \
                matrix[rightDownRow][rightDownCol - i], matrix[rightDownRow - i][leftTopCol], = \
                    matrix[rightDownRow - i][leftTopCol], matrix[leftTopRow][leftTopCol + i], \
                    matrix[leftTopRow + i][rightDownCol], matrix[rightDownRow][rightDownCol - i]

            # 完成旋转后更新层级
            leftTopRow += 1
            leftTopCol += 1
            rightDownRow -= 1
            rightDownCol -= 1


if __name__ == '__main__':
    s = Solution()
    matrix = [[5, 1, 9, 11],
              [2, 4, 8, 10],
              [13, 3, 6, 7],
              [15, 14, 12, 16]]
    s.rotate(matrix)
    for line in matrix:
        print(line)
