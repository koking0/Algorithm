def judge(num):
	num_list = list(str(num))
	return False if 'B' in num_list or '4' in num_list else True


if __name__ == '__main__':
	ans = 0
	for i in range(1, 2019):
		for j in range(i + 1, 2019):
			if (2019 - i - j) > j and judge(i) and judge(j) and judge(2019 - i - j):
				ans += 1
				print(f"ans = {ans}, {i} + {j} + {2019 - i - j} = 2019")
	print(ans)
