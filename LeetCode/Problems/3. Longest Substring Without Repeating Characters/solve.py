class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		left, res, idx = -1, 0, {}  # idx 表示某字符出现的索引
		for i, ch in enumerate(s):
			if ch in idx and idx[ch] > left:  # 如果 ch 在字典中并且上次出现的索引大于当前长度的下标
				left = idx[ch]
			else:
				res = max(res, i - left)
			idx[ch] = i
		return res


if __name__ == '__main__':
	a = Solution()
	print(a.lengthOfLongestSubstring("pwwkew"))
