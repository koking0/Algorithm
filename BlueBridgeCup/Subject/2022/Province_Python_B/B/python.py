def check(n):
	if n % 2 == 1 and \
		n % 3 == 2 and \
		n % 4 == 1 and \
		n % 5 == 4 and \
		n % 6 == 5 and \
		n % 7 == 4 and \
		n % 8 == 1 and \
		n % 9 == 2 and \
		n % 10 == 9 and \
		n % 11 == 0 and \
		n % 12 == 5 and \
		n % 13 == 10 and \
		n % 14 == 11 and \
		n % 15 == 14 and \
		n % 16 == 9 and \
		n % 17 == 0 and \
		n % 18 == 11 and \
		n % 19 == 18 and \
		n % 20 == 9 and \
		n % 21 == 11 and \
		n % 22 == 11 and \
		n % 23 == 15 and \
		n % 24 == 17 and \
		n % 25 == 9 and \
		n % 26 == 23 and \
		n % 27 == 20 and \
		n % 28 == 25 and \
		n % 29 == 16 and \
		n % 30 == 29 and \
		n % 31 == 27 and \
		n % 32 == 25 and \
		n % 33 == 11 and \
		n % 34 == 17 and \
		n % 35 == 4 and \
		n % 36 == 29 and \
		n % 37 == 22 and \
		n % 38 == 37 and \
		n % 39 == 23 and \
		n % 40 == 9 and \
		n % 41 == 1 and \
		n % 42 == 11 and \
		n % 43 == 11 and \
		n % 44 == 33 and \
		n % 45 == 29 and \
		n % 46 == 15 and \
		n % 47 == 5 and \
		n % 48 == 41 and \
		n % 49 == 46:
		return True


def solve1():
	max_num = 100000000000000000
	print(f"max 11 num = {max_num // 11}")
	print(f"max 17 num = {max_num // 17}")
	for i in range(1, (max_num // 11) + 1):
		for j in range(1, (max_num // 17) + 1):
			num = (11 * i) * (17 * j)
			if check(num):
				print(f"num = {num}")
				return
	print("What Fuck!")


def solve2():
	num = 1
	max_num = 100000000000000000
	while num < max_num:
		idx_1 = 1
		num = num * (idx_1 * 11)
		
		idx_2 = 1
		while num < max_num:
			num = num * (idx_2 * 17)
			print(num)
			if check(num):
				print(f"num = {num}")
				return
			idx_2 += 1
		idx_1 += 1
	print("What Fuck!")


def solve3():
	num = 11 * 17
	max_num = 100000000000000000
	for i in range(1, (max_num // (11 * 17)) + 1):
		num *= i
		if check(num):
			print(f"num = {num}")
			return
	print("What Fuck!")


def solve4():
	max_num = 100000000
	for num in range(1, max_num):
		if check(num):
			print(f"num = {num}")
	print("What Fuck!")


if __name__ == '__main__':
	# solve1()
	# solve2()
	solve3()
	# solve4()
