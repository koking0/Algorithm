def check(a: int) -> bool:
	thirdPower = str(a ** 3)
	fourthPower = str(a ** 4)
	return len(thirdPower) == 4 and len(fourthPower) == 6 and len(set(list(thirdPower + fourthPower))) == 10


if __name__ == '__main__':
	for age in range(100):
		if check(age):
			print(age)
