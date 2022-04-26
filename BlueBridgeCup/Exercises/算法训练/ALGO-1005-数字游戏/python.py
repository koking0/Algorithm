# -*- coding: utf-8 -*-
# @Time        : 2022/4/26 13:17
# @File        : python.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from math import comb
from itertools import permutations


def check(item):
	res = 0
	for i in range(n):
		res += xi_shu[i] * item[i]
		if res > ans:
			return False
	return res == ans


def solve():
	for item in permutations(range(1, n + 1)):
		if check(item):
			print(' '.join(map(str, item)))
			return


if __name__ == '__main__':
	n, ans = map(int, input().split())
	xi_shu = [comb(n - 1, i) for i in range(n)]
	solve()
