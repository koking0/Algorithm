from collections import deque

def map_fun(d, p ,q):
	if d == 0:
		return 0, p, q
	if d == 1:
		return 0, p - q, p
	if d == 2:
		return 0, -q, p - q
	if d == 3:
		return 0, -p, -q
	if d == 4:
		return 0, q - p, -p
	if d == 5:
		return 0, q, q - p


def solve():
	visit = set()
	queue = deque()
	queue.append((d1, p1, q1, 0))
	visit.add((d1, p1, q1))
	
	while queue:
		d, p, q, l = queue.popleft()
		if (d, p, q) == (d2, p2, q2):
			print(l)
			return
		
		for dd, dp, dq in [(0, 1, 0), (0, 1, 1), (0, 0, 1), (0, -1, 0), (0, -1, -1), (0, 0, -1)]:
			nd, np, nq = d + dd, p + dp, q + dq
			if (nd, np, nq) not in visit:
				queue.append((nd, np, nq, l + 1))
				visit.add((nd, np, nq))
			

if __name__ == '__main__':
	d1, p1, q1, d2, p2, q2 = map(int, input().split())
	d1, p1, q1 = map_fun(d1, p1, q1)
	d2, p2, q2 = map_fun(d2, p2, q2)
	# 先把坐标都映射为从 0 方向开始
	solve()
