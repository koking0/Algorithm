from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def process_ans():
            if left_up_x == right_down_x:
                for i in range(left_up_y, right_down_y + 1):
                    ans.append(matrix[left_up_x][i])
            elif left_up_y == right_down_y:
                for i in range(left_up_x, right_down_x + 1):
                    ans.append(matrix[i][left_up_y])
            else:
                cur_x, cur_y = left_up_x, left_up_y
                while cur_y != right_down_y:
                    ans.append(matrix[left_up_x][cur_y])
                    cur_y += 1
                while cur_x != right_down_x:
                    ans.append(matrix[cur_x][right_down_y])
                    cur_x += 1
                while cur_y != left_up_y:
                    ans.append(matrix[right_down_x][cur_y])
                    cur_y -= 1
                while cur_x != left_up_x:
                    ans.append(matrix[cur_x][left_up_y])
                    cur_x -= 1

        ans = []
        left_up_x, left_up_y = 0, 0
        right_down_x, right_down_y = len(matrix) - 1, len(matrix[0]) - 1
        while left_up_x <= right_down_x and left_up_y <= right_down_y:
            process_ans()
            left_up_x += 1
            left_up_y += 1
            right_down_x -= 1
            right_down_y -= 1
        return ans


if __name__ == '__main__':
    print(Solution().spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
