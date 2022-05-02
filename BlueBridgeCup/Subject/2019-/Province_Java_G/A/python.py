def check(num: int) -> bool:
	for item in list(str(num)):
		if item in ['B', '0', '1', '9']:
			return True
	return False


if __name__ == '__main__':
	n = 2019
	ans = 0
	for i in range(1, n + 1):
		if check(i):
			ans += i ** 3
	print(ans)
