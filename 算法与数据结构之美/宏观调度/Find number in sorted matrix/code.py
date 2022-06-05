#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/1/21 上午10:57
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
import random


def find_number(input_matrix, number):
    row, col = 0, len(input_matrix[0]) - 1
    print('To find ', number, ' in matrix')
    while row < len(input_matrix) and col > -1:
        if input_matrix[row][col] == number:
            return row, col
        elif input_matrix[row][col] > number:
            col -= 1
        else:
            row += 1
    return None


if __name__ == '__main__':
    matrix = [[1, 2,  3,  4,  5,  6,  7,  8,  9],
              [2, 4,  6,  8,  10, 12, 14, 16, 18],
              [3, 6,  9,  12, 15, 18, 21, 24, 27],
              [4, 8,  12, 16, 20, 24, 28, 32, 36],
              [5, 10, 15, 20, 25, 30, 35, 40, 45]]
    print(find_number(matrix, random.randint(0, 46)))
