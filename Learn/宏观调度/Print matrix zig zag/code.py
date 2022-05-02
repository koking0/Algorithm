#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/1/20 下午3:47
# @File     : BubbleSortCode.py
# @Project  : Algorithm
# @Software : PyCharm
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


def print_diagonal_line(input_matrix, a_row, a_col, b_row, b_col, flag):
    if flag:
        while a_row != b_row + 1:
            print(input_matrix[a_row][a_col], end=' ')
            a_row += 1
            a_col -= 1
    else:
        while b_row != a_row - 1:
            print(input_matrix[b_row][b_col], end=' ')
            b_row -= 1
            b_col += 1


def print_matrix_zig_zag(input_matrix):
    a_row, a_col, b_row, b_col, end_row, end_col, flag = \
        0, 0, 0, 0, len(input_matrix) - 1, len((matrix[0])) - 1, False
    while a_row != end_row + 1:
        print_diagonal_line(input_matrix, a_row, a_col, b_row, b_col, flag)
        [a_row, a_col, b_row, b_col, flag] = \
            [a_row + 1 if a_col == end_col else a_row,
             a_col if a_col == end_col else a_col + 1,
             b_row if b_row == end_row else b_row + 1,
             b_col + 1 if b_row == end_row else b_col, bool(1 - flag)]


if __name__ == '__main__':
    matrix = [[1,  2,  3,  4],
              [5,  6,  7,  8],
              [9,  10, 11, 12],
              [13, 14, 15, 16]]
    for i in matrix:
        print(i)
    print_matrix_zig_zag(matrix)
