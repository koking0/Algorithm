#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/9 H:51
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
from typing import List


class Solution:
	def restoreIpAddresses(self, s: str) -> List[str]:
		ans = []
		if len(s) > 12:
			return ans
		for i in range(1, len(s)):
			for j in range(i + 1, len(s)):
				for k in range(j + 1, len(s)):
					nums = [s[:i], s[i:j], s[j:k], s[k:]]
					for item in nums:
						if not item or (len(item) > 1 and item[0] == '0') or not (0 <= int(item) <= 255):
							break
					else:
						ans.append('.'.join(nums))
		return ans


a = Solution()
print(a.restoreIpAddresses("0000"))
