# -*- coding: utf-8 -*-
# @Time        : 2022/1/24 8:58
# @File        : python.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
def solve():
	queue = list()
	n = int(input())
	for _ in range(n):
		string = input()
		if string[0] == '1':  # 入队操作
			queue.append(string.split(' ')[1])
		elif string[0] == '2':  # 出队操作
			if queue:
				print(queue.pop(0))
			else:
				print("no")
				return
		elif string[0] == '3':  # 计算队中元素个数并输出
			print(len(queue))


if __name__ == '__main__':
	solve()
