def solve1():
	matrix = [[1], [1, 1]]
	ans = 3
	while n not in matrix[-1]:
		cur = [1]
		for i in range(1, len(matrix[-1])):
			cur.append(matrix[-1][i] + matrix[-1][i - 1])
		cur.append(1)
		matrix.pop(0)
		matrix.append(cur)
		ans += len(cur)
	print(ans - (len(matrix[-1]) - matrix[-1].index(n)) + 1)


def comb(a, b):
	res = 1
	i = a
	j = 1
	while j <= b:
		res = res * i / j
		i -= 1
		j += 1
		if res > n:
			return res
	return res


def check(x):
	left, right = 2 * x, n
	while right > left:
		middle = (left + right) >> 1
		if comb(middle, x) < n:
			left = middle + 1
		else:
			right = middle
	if comb(right, x) == n:
		print((int(((1 + right) * right) / 2) + x + 1))
		return True
	return False


if __name__ == '__main__':
	n = int(input())
	if n == 1:
		print(1)
	else:
		for num in range(16, -1, -1):
			if check(num):
				break
