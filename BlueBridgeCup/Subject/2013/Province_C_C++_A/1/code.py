import datetime

if __name__ == '__main__':
	birth = datetime.datetime.strptime("1777-04-30", "%Y-%m-%d")
	new = birth + datetime.timedelta(days=8112)
	print(new)
