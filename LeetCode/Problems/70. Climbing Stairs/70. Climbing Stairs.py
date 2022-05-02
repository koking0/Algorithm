#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/13 10:00
# @File     : 70. Climbing Stairs.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class Solution:
    def climbStairs_recursion(self, n: int) -> int:
        def solve(num):
            if num == 1:
                return 1
            if num == 2:
                return 2
            return solve(num - 1) + solve(num - 2)

        return solve(n)

    def climbStairs_dynamic_programming(self, n: int) -> int:
        f0, f1, ans = 0, 0, 1
        for i in range(1, n + 1):
            f0 = f1
            f1 = ans
            ans = f0 + f1
        return ans

    def climbStairs_matrix_fast_power(self, n: int) -> int:
        def multiply(matrixA, matrixB):
            ans = []
            for i in range(2):
                ans.append([])
                for j in range(2):
                    ans[i].append(matrixA[i][0] * matrixB[0][j] + matrixA[i][1] * matrixB[1][j])
            return ans

        def solve(matrix, num):
            ret = [[1, 0], [0, 1]]
            while num > 0:
                if (num & 1) == 1:
                    ret = multiply(ret, matrix)
                num >>= 1
                matrix = multiply(matrix, matrix)
            return ret

        M = [[1, 1], [1, 0]]
        res = solve(M, n)
        return res[0][0]


a = Solution()
print(a.climbStairs_matrix_fast_power(2))
