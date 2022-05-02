def gcd(a, b):
	return a if b == 0 else gcd(b, a % b)


if __name__ == '__main__':
	p, q = map(int, input().split())
	num = int(input())
	m, n = p - 1, q - p + 1
	k = int(num / (10 ** n))
	l = int(num % (10 ** n))
	x, y = k * (10 ** n - 1) + l, (10 ** n - 1) * (10 ** m)
	g = gcd(x, y)
	x, y = x / g, y / g
	print(f"{int(x)} {int(y)}")
