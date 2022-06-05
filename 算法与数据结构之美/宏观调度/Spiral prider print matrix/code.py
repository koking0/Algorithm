def print_edge(temp_matrix, left_up_x, left_up_y, right_down_x, right_down_y):
    if left_up_x == right_down_x:
        for i in range(left_up_y, right_down_y + 1):
            print(temp_matrix[left_up_x][i], end=' ')
    elif left_up_y == right_down_y:
        for i in range(left_up_x, right_down_x):
            print(temp_matrix[i][left_up_y], end=' ')
    else:
        cur_x = left_up_x
        cur_y = left_up_y
        while cur_y != right_down_y:
            print(temp_matrix[left_up_x][cur_y], end=' ')
            cur_y += 1
        while cur_x != right_down_x:
            print(temp_matrix[cur_x][right_down_y], end=' ')
            cur_x += 1
        while cur_y != left_up_y:
            print(temp_matrix[right_down_x][cur_y], end=' ')
            cur_y -= 1
        while cur_x != left_up_x:
            print(temp_matrix[cur_x][left_up_y], end=' ')
            cur_x -= 1


def spiral_prider_print(input_matrix):
    left_up_x = 0
    left_up_y = 0
    right_down_x = len(input_matrix[0]) - 1
    right_down_y = len(input_matrix) - 1
    while left_up_x <= right_down_x and left_up_y < right_down_y:
        print_edge(input_matrix, left_up_x, left_up_y, right_down_x, right_down_y)
        left_up_x += 1
        left_up_y += 1
        right_down_x -= 1
        right_down_y -= 1


if __name__ == '__main__':
    matrix = [[1,  2,  3,  4],
              [5,  6,  7,  8],
              [9,  10, 11, 12],
              [13, 14, 15, 16]]
    spiral_prider_print(matrix)
