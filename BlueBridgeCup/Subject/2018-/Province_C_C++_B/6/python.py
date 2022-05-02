from bisect import bisect_left, bisect_right

if __name__ == '__main__':
	ans = 0
	n = int(input())
	A = sorted(list(map(int, input().split())))
	B = sorted(list(map(int, input().split())))
	C = sorted(list(map(int, input().split())))
	
	for item in B:
		num_1 = bisect_left(A, item)
		num_2 = n - bisect_right(C, item)
		print(num_1, num_2)
		ans += num_1 * num_2
	print(ans)
