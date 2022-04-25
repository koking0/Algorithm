# -*- coding: utf-8 -*-
# @Time        : 2022/1/26 13:07
# @File        : python.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
def check(date):
	def is_leap_year(y):
		return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0

	year = 1900 + date[0] if date[0] > 59 else 2000 + date[0]
	days = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if 0 < date[1] < 13:
		if 0 < date[2] < days[date[1] - 1] + 1:
			return f"{year}-{str(date[1]).zfill(2)}-{str(date[2]).zfill(2)}"


if __name__ == '__main__':
	aa, bb, cc = map(int, input().split('/'))

	ans = set()
	if check((aa, bb, cc)):
		ans.add(check((aa, bb, cc)))
	if check((cc, aa, bb)):
		ans.add(check((cc, aa, bb)))
	if check((cc, bb, aa)):
		ans.add(check((cc, bb, aa)))
	ans = list(ans)
	ans.sort()
	print("\n".join(ans))
