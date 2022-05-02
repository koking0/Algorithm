# -*- coding: utf-8 -*-
# @Time        : 2022/4/25 20:29
# @File        : PREV-72-组合数问题.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
def solve():
	n, m = map(int, input().split())
	for i in range(1, n + 1):
		for j in range(0, min(i, m) + 1):
			pass


if __name__ == '__main__':
	t, k = map(int, input().split())
	for _ in range(t):
		solve()
