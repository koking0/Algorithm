# -*- coding: utf-8 -*-
# @Author   : Alex
# @Time     : 2022/6/5 10:34
# @File     : python.py
# @Software : PyCharm
# Email     : liu_zhao_feng_alex@163.com
# Blog      : https://alex007.blog.csdn.net/
class Solution:
	def reversePrefix(self, word: str, ch: str) -> str:
		return word if ch not in word else word[:word.index(ch) + 1][::-1] + word[word.index(ch) + 1:]
