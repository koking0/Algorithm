if __name__ == '__main__':
	N, K = map(int, input().split())
	A = list(map(int, input().split()))
	
	ans = 0
	for i in range(N):
		if i > 0 and i + K < N and A[i] < A[i - 1] <= A[i + K]:
			for t in range(i, i + K):
				A[t] = A[i - 1]
			left, right = i - 1, i + K + 1
			while left > 0 and A[left] >= A[left - 1]:
				left -= 1
			while right + 1 < N and A[right] <= A[right + 1]:
				right += 1
			ans = max(ans, right - left)
	print(ans)
