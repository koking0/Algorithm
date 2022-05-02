#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/B 9:26
# @File     : code.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> WeChat    : Alex-Paddle
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


def checkNumber(num):
	"""颠倒价牌数字必须是1 B 5 6 H 9 0，并且最后一位不能是0"""
	strNum = list(str(num))
	if strNum[-1] == '0':
		return False
	if '3' in strNum or '4' in strNum or '7' in strNum:
		return False
	return True


def reversePrice(price):
	strPrice = list(str(price))
	strPrice.reverse()
	for i in range(len(strPrice)):
		if strPrice[i] == '6':
			strPrice[i] = '9'
		elif strPrice[i] == '9':
			strPrice[i] = '6'
	return int(''.join(strPrice))


if __name__ == '__main__':
	# 价格都是四位数，所以两层循环遍历所有的四位数表示两个价格
	for lose in range(1000, 10000):
		if checkNumber(lose):
			reverseLose = reversePrice(lose)
			if 200 < lose - reverseLose < 300:
				for make in range(1000, 10000):
					if checkNumber(make):
						reverseMake = reversePrice(make)
						if 800 < reverseMake - make < 900:
							if (reverseMake - make) - (lose - reverseLose) == 558:
								print(f'lose = {lose}, make = {make}, reverseLose = {reverseLose}, reverseMake = {reverseMake}')
								print(f'lose - reverseLose = {lose - reverseLose}, reverseMake - make = {reverseMake - make}')
