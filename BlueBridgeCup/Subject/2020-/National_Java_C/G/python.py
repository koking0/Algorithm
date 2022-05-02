def cal(k, x, y):
	if k == 0:
		return 1
	length, cnt = f[k], f[k * 2] / 9
	if x < length / 3:
		if y < length / 3:
			return cal(k - 1, x, y)
		elif y < 2 * length / 3:
			return cnt + cal(k - 1, length / 3 - x - 1, y - length / 3)
		else:
			return 2 * cnt + cal(k - 1, x, y - 2 * length / 3)
	elif x < 2 * length / 3:
		if y < length / 3:
			return 5 * cnt + cal(k - 1, x - length / 3, length / 3 - y - 1)
		elif y < 2 * length / 3:
			return 4 * cnt + cal(k - 1, 2 * length / 3 - x - 1, 2 * length / 3 - y - 1)
		else:
			return 3 * cnt + cal(k - 1, x - length / 3, length - y - 1)
	else:
		if y < length / 3:
			return 6 * cnt + cal(k - 1, x - 2 * length / 3, y)
		elif y < 2 * length / 3:
			return 7 * cnt + cal(k - 1, length - x - 1, y - length / 3)
		else:
			return 8 * cnt + cal(k - 1, x - 2 * length / 3, y - 2 * length / 3)


if __name__ == '__main__':
	f = [1]
	for i in range(1, 40):
		f.append(f[i - 1] * 3)
	# print(f"f = {f}")
	
	k = int(input())
	x1, y1 = map(int, input().split())
	x2, y2 = map(int, input().split())
	
	# print(f"ans1 = {cal(k, x1, y1)}")
	# print(f"ans2 = {cal(k, x2, y2)}")
	print(abs(int(cal(k, x1, y1) - cal(k, x2, y2))))
