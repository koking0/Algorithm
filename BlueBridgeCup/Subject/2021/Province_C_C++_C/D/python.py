if __name__ == '__main__':
	for num in range(1, 1000000008):
		val = (num * 2021) % 1000000007
		if val == 999999999:
			print(num)
