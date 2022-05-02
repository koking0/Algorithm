#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/9 H:41
# @File     : 面试题 17.13. 恢复空格.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import collections
from typing import List


class Trie:
	def __init__(self):
		self.next_nodes = collections.defaultdict(Trie)
		self.isEnd = False


class Solution:
	def respace_dp(self, dictionary: List[str], sentence: str) -> int:
		n = len(sentence)
		dp = [i for i in range(n + 1)]
		for i in range(n):
			for j in range(i, -1, -1):
				if sentence[j:i + 1] in dictionary:
					dp[i + 1] = min(dp[i + 1], dp[j])
				else:
					dp[i + 1] = min(dp[i + 1], dp[i] + 1)
		return dp[-1]

	def respace(self, dictionary, sentence: str) -> int:
		trie = Trie()
		# 初始化字典树
		for word in dictionary:
			cur = trie
			for i in range(len(word) - 1, -1, -1):
				cur = cur.next_nodes[word[i]]
			cur.isEnd = True

		dp = [float('inf') for _ in range(len(sentence) + 1)]
		dp[0] = 0
		for i in range(1, len(sentence) + 1):
			dp[i] = dp[i - 1] + 1

			j = i
			cur = trie
			while j >= 1 and sentence[j - 1] in cur.next_nodes:
				cur = cur.next_nodes[sentence[j]]
				if cur.isEnd:
					dp[i] = min(dp[i], dp[j - 1])
				if dp[i] == 0:
					break
				j -= 1
		return int(dp[-1])
