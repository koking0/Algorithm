import datetime

if __name__ == '__main__':
	for i in range(19, 100):
		day = datetime.datetime.strptime(f'{i}991231', "%Y%m%d").weekday()
		if day + 1 == 7:
			print(f'{i}99-12-31')
			break
