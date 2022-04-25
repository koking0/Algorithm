if __name__ == '__main__':
	for num in range(100000, 1000000):
		square = num ** 2
		if len(set(str(num))) == 6 and not (set(str(num)) & set(str(square))):
			print(f'{num} * {num} = {num ** 2}')
