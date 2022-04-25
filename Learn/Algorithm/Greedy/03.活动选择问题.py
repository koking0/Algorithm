def activitySelection(activities: list):
	activities.sort(key=lambda x: x[1])
	result = [activities[0]]
	for index in range(1, len(activities)):
		if activities[index][0] >= result[-1][1]:
			result.append(activities[index])
	return result


if __name__ == '__main__':
	print(activitySelection([(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (12, 16)]))
