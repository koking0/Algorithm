if __name__ == '__main__':
	n, m = map(int, input().split())
	nums = [i + 1 for i in range(n)]
	
	action_list = []
	for _ in range(m):
		p, q = map(int, input().split())
		if p == 0:
			while action_list and action_list[-1][0] == 0:
				q = max(q, action_list[-1][1])
				action_list.pop()
			while len(action_list) > 1 and action_list[-2][1] <= q:
				action_list.pop()
				action_list.pop()
			action_list.append((0, q))
		elif action_list:
			while action_list and action_list[-1][0] == 1:
				q = min(q, action_list[-1][1])
				action_list.pop()
			while len(action_list) > 1 and action_list[-2][1] >= q:
				action_list.pop()
				action_list.pop()
			action_list.append((1, q))
	
	k, left, right = n, 1, n
	for idx, val in enumerate(action_list):
		if val[0] == 0:
			while right > val[1] and left <= right:
				nums[right - 1] = k
				right -= 1
				k -= 1
		else:
			while left < val[1] and left <= right:
				nums[left - 1] = k
				left += 1
				k -= 1
		if left > right:
			break
	
	if action_list[-1][0] == 0:
		while left <= right:
			nums[left - 1] = k
			left += 1
			k -= 1
	else:
		while left <= right:
			nums[right - 1] = k
			right -= 1
			k -= 1
	
	print(' '.join(map(str, nums)))
