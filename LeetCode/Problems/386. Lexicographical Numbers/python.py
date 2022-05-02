# -*- coding: utf-8 -*-
# @Time        : 2022/1/20 22:22
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
	def lexicalOrder(self, n: int) -> List[int]:
		num_list = list(range(1, n + 1))
		str_list = list(map(str, num_list))
		str_list.sort()
		return list(map(int, str_list))


if __name__ == '__main__':
	print(Solution().lexicalOrder(13))
