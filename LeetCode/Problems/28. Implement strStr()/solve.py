class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		def get_next_index(array):
			length = len(array)
			if length == 1:
				return [-1]

			idx, cnt, next_index = 2, 0, [-1, 0]
			while idx < length:
				if array[idx - 1] == array[cnt]:
					next_index.append(cnt + 1)
					idx += 1
					cnt += 1
				elif cnt > 0:
					cnt = next_index[cnt]
				else:
					next_index.append(0)
					idx += 1
			return next_index

		def KMP(pattern, target):
			if not target:
				return 0
			if not pattern or len(pattern) < len(target):
				return -1

			pattern, target = list(pattern), list
