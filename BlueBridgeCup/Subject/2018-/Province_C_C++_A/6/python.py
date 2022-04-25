# -*- coding: utf-8 -*-
# @Time        : 2022/2/27 14:27
# @File        : python.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
def process_time(time_string):
	time_list = time_string.split()
	time_1, time_2 = list(map(int, time_list[0].split(':'))), list(map(int, time_list[1].split(':')))
	if len(time_list) == 3:
		time_2[-1] += int(time_list[-1][1:-1]) * 24 * 60 * 60
	(h1, m1, s1), (h2, m2, s2) = time_1, time_2
	return (h2 * 60 * 60 + m2 * 60 + s2) - (h1 * 60 * 60 + m1 * 60 + s1)


if __name__ == '__main__':
	n = int(input())
	for _ in range(n):
		time1 = process_time(input())
		time2 = process_time(input())
		ans = (time1 + time2) // 2
		print(f"{ans // 3600:02}:{ans // 60 % 60:02}:{ans % 60:02}")
