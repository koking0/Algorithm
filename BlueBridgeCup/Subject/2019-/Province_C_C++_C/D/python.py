def is_primer(n):
	for i in range(2, int((n ** 0.5) + 1)):
		if n % i == 0:
			return False
	return True


if __name__ == '__main__':
	num = 2
	primer_num = list()
	while len(primer_num) < 2019:
		if is_primer(num):
			primer_num.append(num)
		num += 1
	print(primer_num[-1])
