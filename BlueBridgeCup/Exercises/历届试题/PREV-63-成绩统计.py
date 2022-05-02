if __name__ == '__main__':
	n = int(input())
	ji_ge_cnt, you_xiu_cnt = 0, 0
	for _ in range(n):
		score = int(input())
		if score > 59:
			ji_ge_cnt += 1
		if score > 84:
			you_xiu_cnt += 1
	print(f"{int(round(100 * ji_ge_cnt / n))}%")
	print(f"{int(round(100 * you_xiu_cnt / n))}%")
