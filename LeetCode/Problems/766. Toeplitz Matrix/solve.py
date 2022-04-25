from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                r, c = i, j
                while r < m and c < n:
                    if matrix[r][c] != matrix[i][j]:
                        return False
                    r, c = r + 1, c + 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isToeplitzMatrix(matrix=[[1, 2], [2, 2]]))
