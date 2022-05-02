if __name__ == '__main__':
	mod = 1000000009
	n, k = map(int, input().split())
	a = [int(input()) for _ in range(n)]
	a.sort()
	
	left, right = 0, n - 1
	res, sign = 1, 1
	if k % 2:
		res = a[right]
		right -= 1
		k -= 1
		if res < 0:
			sign = -1
	
	while k:
		x, y = a[left] * a[left + 1], a[right] * a[right - 1]
		if sign * x > sign * y:
			res = (res * x) % mod
			left += 2
		else:
			res *= y
			right -= 2
		k -= 2
	
	print(-1 * (abs(res) % mod) if res < 0 else res % mod)
