from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        res = [[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                res[j][i] = matrix[i][j]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.transpose(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
