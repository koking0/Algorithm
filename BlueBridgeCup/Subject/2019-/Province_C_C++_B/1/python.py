if __name__ == '__main__':
	team = []
	with open("./team.txt", 'r') as fp:
		for line in fp.readlines():
			line = line.strip("\n").strip(',')
			team.append(eval(line))

	peoples, ans = len(team), 0
	for a in range(peoples):
		for b in range(peoples):
			if b != a:
				for c in range(peoples):
					if c != b and c != a:
						for d in range(peoples):
							if d != c and d != b and d != a:
								for e in range(peoples):
									if e != d and e != c and e != b and e != a:
										ans = max(ans, team[a][1] + team[b][2] + team[c][3] + team[d][4] + team[e][5])
	print(ans)
