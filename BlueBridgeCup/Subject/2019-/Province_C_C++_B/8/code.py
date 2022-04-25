def gcd(a, b):
	return gcd(b, a % b) if b else a


if __name__ == '__main__':
	n = int(input())
	nums = list(map(int, input().split(' ')))
	nums.sort()
	diff = [nums[i] - nums[i - 1] for i in range(1, n)]
	ans = gcd(diff[0], diff[1])
	for i in range(2, len(diff)):
		ans = gcd(ans, diff[i])
	print(((nums[-1] - nums[0]) // ans) + 1)
