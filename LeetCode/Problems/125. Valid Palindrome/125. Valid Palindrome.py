#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/19 9:23
# @File     : 125. Valid Palindrome.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class Solution:
	def isPalindrome(self, s: str) -> bool:
		import string
		# 1.去掉所有的空格
		s = s.replace(" ", "")
		# B.去掉所有的标点符号
		s = "".join(c for c in s if c not in string.punctuation)
		# 3.把所有的单词变成小写
		s = s.lower()
		# 4.验证回文串
		return s == s[::-1]


if __name__ == '__main__':
	a = Solution()
	print(a.isPalindrome("A man, a plan, a canal: Panama"))
