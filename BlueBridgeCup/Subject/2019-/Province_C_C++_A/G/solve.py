if __name__ == '__main__':
	n, m, t = map(int, input().split())
	ts_ids, scores, time_dict, ans = [], [0] * n, {}, []
	for _ in range(m):
		ts_ids.append(list(map(int, input().split())))
	ts_ids.sort(key=lambda x: x[0])
	for item in ts_ids:
		if time_dict.get(item[0], None):
			time_dict[item[0]].append(item[1])
		else:
			time_dict[item[0]] = [item[1]]
	for time in range(1, t):
		for store in range(1, n + 1):
			if time in time_dict.keys() and store in time_dict[time]:
				scores[store - 1] += (2 * time_dict[time].count(store))
			else:
				scores[store - 1] = max(scores[store - 1] - 1, 0)
			if scores[store - 1] > 5 and store not in ans:
				ans.append(store)
			elif scores[store - 1] < 4 and store in ans:
				ans.remove(store)
	print(len(ans))
