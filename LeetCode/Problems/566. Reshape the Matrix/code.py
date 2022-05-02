from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(nums), len(nums[0])
        if rows * cols != r * c:
            return nums

        arr = []
        for i in range(rows):
            for j in range(cols):
                arr.append(nums[i][j])
        ans = [[None for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                ans[i][j] = arr.pop(0)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.matrixReshape(nums=[[1, 2], [3, 4]], r=1, c=4))
