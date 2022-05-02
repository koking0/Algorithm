# -*- coding: utf-8 -*-
# @Time        : 2022/1/25 21:53
# @File        : python.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from collections import deque


class MyStack:

	def __init__(self):
		self.q1, self.q2 = deque(), deque()

	def push(self, x: int) -> None:
		self.q1.append(x)

	def pop(self) -> int:
		return self.q1.pop()

	def top(self) -> int:
		return self.q1[-1]

	def empty(self) -> bool:
		return len(self.q1) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
