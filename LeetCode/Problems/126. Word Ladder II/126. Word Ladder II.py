#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/7 H:30
# @File     : 126. Word Ladder II.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from collections import defaultdict, deque
from typing import List


class Solution:
	def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
		length = len(beginWord)
		wordList.append(beginWord)
		# 构建具有邻接关系的桶
		buckets = defaultdict(list)
		for word in wordList:
			for i in range(length):
				match = word[:i] + '_' + word[i + 1:]
				buckets[match].append(word)
		print(buckets)
		# BFS遍历
		preWords = defaultdict(list)  # 前溯词列表
		toSeen = deque([(beginWord, 1)])  # 待遍历词及深度列表
		beFound = {beginWord: 1}  # 已探测词词列表
		while toSeen:
			curWord, level = toSeen.popleft()
			for i in range(len(beginWord)):
				match = curWord[:i] + '_' + curWord[i + 1:]
				for word in buckets[match]:
					if word not in beFound:
						beFound[word] = level + 1
						toSeen.append((word, level + 1))
					if beFound[word] == level + 1:  # 当前深度等于该词首次遍历深度，则仍应加入前溯词列表
						preWords[word].append(curWord)
			if endWord in beFound and level + 1 > beFound[endWord]:  # 已搜索到目标词，且完成当前层遍历
				break
		# 列表推导式输出结果
		if endWord in beFound:
			res = [[endWord]]
			while res[0][0] != beginWord:
				res = [[word] + r for r in res for word in preWords[r[0]]]
			return res
		else:
			return []


a = Solution()
print(a.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
