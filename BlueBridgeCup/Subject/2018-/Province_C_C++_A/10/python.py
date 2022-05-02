if __name__ == '__main__':
	n, s = map(int, input().split())
	money_list = list(map(int, input().split()))
	money_list.sort()
	
	mean, cur_mean, ans = s / n, s / n, 0
	for i in range(n):
		if money_list[i] <= cur_mean:
			s -= money_list[i]
			ans += (mean - money_list[i]) ** 2
			cur_mean = s / (n - i - 1)
		else:
			ans += (cur_mean - mean) ** 2
	
	print(f"{(ans / n) ** 0.5:.4f}")
