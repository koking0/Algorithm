from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def process_ans():
            nonlocal idx
            if left_up_x == right_down_x:
                for i in range(left_up_y, right_down_y + 1):
                    ans[left_up_x][i] = idx
                    idx += 1
            elif left_up_y == right_down_y:
                for i in range(left_up_x, right_down_x + 1):
                    ans[i][left_up_y] = idx
                    idx += 1
            else:
                cur_x, cur_y = left_up_x, left_up_y
                while cur_y != right_down_y:
                    ans[left_up_x][cur_y] = idx
                    idx += 1
                    cur_y += 1
                while cur_x != right_down_x:
                    ans[cur_x][right_down_y] = idx
                    idx += 1
                    cur_x += 1
                while cur_y != left_up_y:
                    ans[right_down_x][cur_y] = idx
                    idx += 1
                    cur_y -= 1
                while cur_x != left_up_x:
                    ans[cur_x][left_up_y] = idx
                    idx += 1
                    cur_x -= 1

        idx, ans = 1, [[0 for _ in range(n)] for i in range(n)]
        left_up_x, left_up_y = 0, 0
        right_down_x, right_down_y = n - 1, n - 1
        while left_up_x <= right_down_x and left_up_y <= right_down_y:
            process_ans()
            left_up_x += 1
            left_up_y += 1
            right_down_x -= 1
            right_down_y -= 1
        return ans


if __name__ == '__main__':
    print(Solution().generateMatrix(3))
