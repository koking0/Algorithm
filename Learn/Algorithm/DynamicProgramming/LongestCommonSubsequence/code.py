def LcsTraceBack(dp, directions, string, length1, length2):
	s = []
	# dp数组不为None时
	while dp[length1][length2]:
		char = directions[length1][length2]
		# 匹配成功，插入该字符，并向左上角找下一个
		if char == 'ok':
			s.append(string[length1 - 1])
			length1 -= 1
			length2 -= 1
		# 根据标记，向左找下一个
		if char == 'left':
			length2 -= 1
		# 根据标记，向上找下一个
		if char == 'up':
			length1 -= 1
	s.reverse()
	return ''.join(s)


def Lcs(str1, str2):
	length1, length2 = len(str1), len(str2)
	# 生成字符串长度加 1 的 0 矩阵 DP 用来保存对应位置匹配的结果
	DP = [[0 for _ in range(length2 + 1)] for _ in range(length1 + 1)]
	# direction 用来记录转移方向
	directions = [['' for _ in range(length2 + 1)] for _ in range(length1 + 1)]

	for p1 in range(length1):
		for p2 in range(length2):
			# 字符匹配成功，则该位置的值为左上方的值加 1
			if str1[p1] == str2[p2]:
				DP[p1 + 1][p2 + 1] = DP[p1][p2] + 1
				directions[p1 + 1][p2 + 1] = 'ok'
			# 左值大于上值，则该位置的值为左值，并标记回溯时的方向为 left
			elif DP[p1 + 1][p2] > DP[p1][p2 + 1]:
				DP[p1 + 1][p2 + 1] = DP[p1 + 1][p2]
				directions[p1 + 1][p2 + 1] = 'left'
			# 上值大于左值，则该位置的值为上值，并标记回溯时的方向为 up
			else:
				DP[p1 + 1][p2 + 1] = DP[p1][p2 + 1]
				directions[p1 + 1][p2 + 1] = 'up'
	return LcsTraceBack(DP, directions, str1, length1, length2), directions


if __name__ == '__main__':
	answer, direction = Lcs('32145', '12345')
	print(answer)
