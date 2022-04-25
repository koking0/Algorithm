# -*- coding: utf-8 -*-
# @Time        : 2022/1/20 21:44
# @File        : python.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
def solve(num):
	hash_table = dict()
	for c in range(int(num ** 0.5) + 1):
		for d in range(c, int(num ** 0.5) + 1):  # d可以从c开始枚举
			val = c ** 2 + d ** 2
			if not hash_table.get(val, None):
				hash_table[val] = f"{c} {d}"
	for a in range(int(num ** 0.5) + 1):
		for b in range(a, int(num ** 0.5) + 1):
			val = hash_table.get(num - a ** 2 - b ** 2)
			if val:
				print(f"{a} {b} {val}")
				return


if __name__ == '__main__':
	solve(int(input()))
