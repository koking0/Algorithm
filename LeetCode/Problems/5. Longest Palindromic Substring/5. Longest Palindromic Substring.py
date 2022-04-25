class Solution:
	def longestPalindrome(self, s: str) -> str:
		n, ans = len(s), ""
		dp = [[False] * n for _ in range(n)]
		for l in range(n):
			for i in range(n):
				j = i + l
				if j >= len(s):
					break
				if l == 0:
					dp[i][j] = True
				elif l == 1:
					dp[i][j] = (s[i] == s[j])
				else:
					dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
				if dp[i][j] and l + 1 > len(ans):
					ans = s[i: j + 1]
		return ans

	def longestPalindrome_violence(self, s: str) -> str:
		if len(s) == 1:
			return s

		for i in range(int(len(s) / 2)):
			if s[i] != s[len(s) - i - 1]:
				break
		else:
			return s

		substring = ""

		for i in range(len(s)):
			for j in range(i + 1, len(s) + 1):
				substring_temp = s[i:j]
				substring_length = len(substring_temp)

				for k in range(int(1 + substring_length / 2)):
					if substring_temp[k] != substring_temp[substring_length - k - 1]:
						break
				else:
					if substring_length > len(substring):
						substring = substring_temp
		return substring

	def longestPalindrome_manacher(self, s: str) -> str:
		def expand(s, left, right):
			while left > -1 and right < len(s) and s[left] == s[right]:
				left -= 1
				right += 1
			return (right - left - 2) // 2

		arm_len = []
		start, end, C, R = 0, -1, -1, -1
		s = '#' + '#'.join(list(s)) + '#'
		for i in range(len(s)):
			if R >= i:
				i_mirror = 2 * C - i
				min_arm_len = min(arm_len[i_mirror], R - i)
				cur_arm_len = expand(s, i - min_arm_len, i + min_arm_len)
			else:
				cur_arm_len = expand(s, i, i)
			arm_len.append(cur_arm_len)
			if i + cur_arm_len > R:
				C = i
				R = i + cur_arm_len
			if 2 * cur_arm_len + 1 > end - start:
				start = i - cur_arm_len
				end = i + cur_arm_len
		return s[start + 1:end + 1:2]
