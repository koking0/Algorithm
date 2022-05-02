from math import floor


def solve():
	A_dict = {"A0": (1189, 841)}
	for i in range(1, 10):
		A_dict[f"A{i}"] = (min(A_dict[f"A{i - 1}"]), floor(max(A_dict[f"A{i - 1}"]) / 2))
	key = input()
	print(max(A_dict[key]))
	print(min(A_dict[key]))


if __name__ == '__main__':
	solve()
