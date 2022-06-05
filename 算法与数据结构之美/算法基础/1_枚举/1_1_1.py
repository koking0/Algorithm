# -*- coding: utf-8 -*-
# @Author   : Alex
# @Time     : 2022/5/5 17:16
# @File     : 1_1_1.py
# @Software : PyCharm
# Email     : liu_zhao_feng_163.com
# Blog      : https://alex007.blog.csdn.net/
def check_prime(num):
	for i in range(2, int(num ** 0.5) + 1):
		if num % i == 0:
			return False
	return True


if __name__ == '__main__':
	n = int(input())
	for a in range(100, 1000):
		for b in range(2, 80):
			if check_prime(b) and a % b == 0 and int(a / b) == n:
				print(f"{a} / {b} = {n}")
