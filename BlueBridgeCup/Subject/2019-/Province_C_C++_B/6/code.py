def check(num):
	strNumList = list(str(num))
	if 'B' in strNumList or '0' in strNumList or '1' in strNumList or '9' in strNumList:
		return True
	return False


if __name__ == '__main__':
	n, ans = int(input()), 0
	for i in range(1, n + 1):
		if check(i):
			ans += i
	print(ans)
