def check(num):
	for ch in ['B', '0', '1', '9']:
		if ch in str(num):
			return True
	return False


if __name__ == '__main__':
	ans1, ans2 = 0, 0
	for i in range(1, 2020):
		if check(i):
			ans1 += i
			ans2 += i ** 2
	print(ans1)
	print(ans2)
