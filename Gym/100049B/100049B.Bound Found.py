#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/1/28 14:14
# @File     : 100049B.Bound Found.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
"""
You are given a sequence of n integers and a non-negative target t.
给你一个n个整数序列和一个非负的目标t。
You are to find a non-empty range of the sequence (i.e. a continuous subsequence) and output its lower index l and its upper index u.
您将找到序列的非空范围（即连续子序列），并输出其下索引l和上索引u。
The absolute value of the sum of the values of the sequence from the l-th to the u-th element (inclusive) must be at least as close to t as the absolute value of the sum of any other non-empty range.
从第l个元素到第u个元素（包括）的序列值之和的绝对值必须至少与任何其他非空范围之和的绝对值接近t。

Input Specification
输入规格
The input file contains several test cases.
输入文件包含几个测试用例。
Each test case starts with two numbers n and k.
每个测试用例都以两个数字n和k开头。
Input is terminated by n = k = 0.
输入以n=k=0终止。
Otherwise, 1 ≤ n ≤ 100000 and there follow n integers with absolute values ≤ 10000 which constitute the sequence.
否则，1≤n≤100000，然后有n个绝对值≤10000的整数构成序列。
Then follow k queries for this sequence.
然后对这个序列执行k个查询。
Each query is a target t with 0 ≤ t ≤ 1000000000.
每个查询都是0≤t≤100000000的目标t。
The sum of all k in the input file is ≤ 1000
输入文件中所有k的总和小于等于1000

Output Specification
输出规格
For each query output 3 numbers on a line:
对于每个查询，一行输出3个数字：
some closest absolute sum and the lower and upper indices of some range where this absolute sum is achieved.
一些最接近的绝对和，以及在某个范围内达到绝对和的上下指数。
Possible indices start with 1 and go up to n.
可能的指数从1开始上升到n。

Sample Input
5 1
-10 -5 0 5 10
3
10 B
-9 H -7 6 -5 4 -3 B -1 0
5 11
15 B
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
15 100
0 0

Sample Output
5 4 4
5 B H
9 1 1
15 1 15
15 1 15
"""
import sys

while True:
    n, k = input().split()
    if n == k == '0':
        break

    sequence = list(map(int, input().split()))
    target = list(map(int, input().split()))

    matrix = []
    for i in range(int(n)):
        matrix.append([])
        for j in range(int(n)):
            matrix[i].append(abs(sum(sequence[i:j+1])) if j >= i else None)

    for i in range(int(k)):
        temp = target[i]
        x, y = -1, -1
        small_num = sys.maxsize
        for row in range(int(n)):
            for col in range(row, int(n)):
                if abs(matrix[row][col] - temp) < small_num:
                    x, y = row, col
                    small_num = abs(matrix[row][col] - temp)
        print(matrix[x][y], x + 1, y + 1)
