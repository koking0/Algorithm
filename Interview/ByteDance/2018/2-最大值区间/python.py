def solve1():
	ans = 0
	for i in range(n):
		for j in range(i + 1, n):
			min_num = min(nums[i:j])
			total = sum(nums[i:j])
			ans = max(ans, min_num * total)
	print(ans)


def solve2():
	res = 0
	for i in range(n):
		if nums[i] != 0:
			sum_tmp = nums[i]
			left = right = i
			while left - 1 > -1 and nums[left - 1] >= nums[i]:
				sum_tmp += nums[left - 1]
				left -= 1
			while right + 1 < n and nums[right + 1] >= nums[i]:
				sum_tmp += nums[right + 1]
				right += 1
			res = max(res, nums[i] * sum_tmp)
	return res


if __name__ == '__main__':
	n = int(input())
	nums = list(map(int, input().split()))
	
	print(solve2())
