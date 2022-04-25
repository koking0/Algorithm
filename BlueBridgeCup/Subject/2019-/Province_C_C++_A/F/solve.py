if __name__ == '__main__':
	N = int(input())
	A = list(map(int, input().split()))
	cur_index, cur_level = 0, 1
	ans, max_sum = 0, 0
	while cur_index < len(A):
		tmp_sum = sum(A[cur_index: cur_index + 2 ** (cur_level - 1)])
		if tmp_sum > max_sum:
			max_sum = tmp_sum
			ans = cur_level
		cur_index = cur_index + 2 ** (cur_level - 1)
		cur_level += 1
	print(ans)
