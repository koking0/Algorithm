from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i == 0 or grid[i - 1][j] == 0:
                        answer += 1
                    if i == len(grid) - 1 or grid[i + 1][j] == 0:
                        answer += 1
                    if j == 0 or grid[i][j - 1] == 0:
                        answer += 1
                    if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                        answer += 1
        return answer


if __name__ == '__main__':
    s = Solution()
    ans = s.islandPerimeter([[1,1]])
    print(ans)
