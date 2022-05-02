import datetime


def check1(s):
	return s == s[::-1]


def check2(s):
	a, b = s[0], s[1]
	return s == ''.join([a, b, a, b, b, a, b, a])


if __name__ == '__main__':
	dt = input()
	year, month, day = dt[0:4], dt[4:6], dt[6:8]
	date = datetime.date(int(year), int(month), int(day))
	
	ans1, ans2 = 0, 0
	while ans1 == 0 or ans2 == 0:
		date = date + datetime.timedelta(days=1)
		if check1(date.strftime("%Y%m%d")) and ans1 == 0:
			ans1 = date.strftime("%Y%m%d")
		if check2(date.strftime("%Y%m%d")) and ans2 == 0:
			ans2 = date.strftime("%Y%m%d")
	print(ans1)
	print(ans2)
