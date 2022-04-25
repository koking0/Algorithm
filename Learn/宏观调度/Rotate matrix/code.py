#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/1/20 上午10:10
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


def rotate_edge(matrix, left_row, left_col, right_row, right_co1):
    for index in range(right_co1 - left_col):
        [matrix[left_row][left_col + index], matrix[right_row - index][left_col],
         matrix[right_row][right_co1 - index], matrix[left_row + index][right_co1]] \
            = [matrix[right_row - index][left_col], matrix[right_row][right_co1 - index],
               matrix[left_row + index][right_co1], matrix[left_row][left_col + index]]


def rotate_matrix(matrix):
    left_row, left_col, right_row, right_col = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
    while left_row <= right_row and left_col <= right_col:
        rotate_edge(matrix, left_row, left_col, right_row, right_col)
        left_row += 1
        left_col += 1
        right_row -= 1
        right_col -= 1


if __name__ == '__main__':
    m = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]
    for i in m:
        print(i)
    print('-----------')
    rotate_matrix(m)
    for i in m:
        print(i)
