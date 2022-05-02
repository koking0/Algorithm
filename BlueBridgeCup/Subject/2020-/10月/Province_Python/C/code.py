from datetime import date
from datetime import timedelta

if __name__ == '__main__':
	start = date(2000, 1, 1)
	end = date(2020, 10, 2)

	res = 0
	while start < end:
		res += 2 if start.day == 1 or start.weekday() == 0 else 1
		start += timedelta(days=1)
	print(res)
