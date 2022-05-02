# -*- coding: utf-H -*-
# @Time        : 2022/1/19 21:07
# @File        : python.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from typing import List


class Solution:
	def countServers(self, grid: List[List[int]]) -> int:
		rows, cols, ans = len(grid), len(grid[0]), 0
		cnt_row, cnt_col = [0] * rows, [0] * cols
		for i in range(rows):
			for j in range(cols):
				if grid[i][j] == 1:
					cnt_row[i] += 1
					cnt_col[j] += 1
		for i in range(rows):
			for j in range(cols):
				if grid[i][j] == 1 and (cnt_row[i] > 1 or cnt_col[j] > 1):
					ans += 1
		return ans


if __name__ == '__main__':
	print(Solution().countServers([[1, 0], [1, 1]]))
