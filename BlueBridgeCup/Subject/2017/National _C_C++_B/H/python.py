# -*- coding: utf-8 -*-
# @Time        : 2022/1/21 8:42
# @File        : python.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
def get_index():
	w, m, n = map(int, input().split(' '))
	idx, flag, ans = 0, True, []
	for r in range(1 + max(m, n) // w):
		for c in range(w) if flag else range(w - 1, -1, -1):
			idx += 1
			if idx in (m, n):
				ans.append((r, c))

		flag = not flag
		if len(ans) == 2:
			return ans[0], ans[1]


if __name__ == '__main__':
	(r1, c1), (r2, c2) = get_index()
	print(abs(r1 - r2) + abs(c1 - c2))
