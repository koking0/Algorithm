import datetime

if __name__ == '__main__':
	ans = 0
	start = datetime.date(1901, 1, 1)
	end = datetime.date(2000, 12, 31)
	while start != end:
		if start.weekday() == 0:
			ans += 1
		start = start + datetime.timedelta(days=1)
	print(ans)
