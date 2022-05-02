def gcd(a: int, b: int) -> int:
	return a if b == 0 else gcd(b, a % b)


if __name__ == '__main__':
	fen_zi = sum([2 ** i for i in range(20)])
	fen_mu = 2 ** 19
	print(f"分子：{fen_zi}，分母：{fen_mu}，最大公约数：{gcd(fen_zi, fen_mu)}")
