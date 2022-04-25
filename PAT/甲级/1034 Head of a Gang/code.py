class UnionFindSet:
    def __init__(self):
        self.cnt = 0
        self.time = {}
        self.gangs = {}
        self.father = {}

    def add(self, n: str, t: int):
        if not self.father.get(n, None):
            self.father[n] = n
            self.time[n] = t
            self.cnt += 1
        else:
            self.time[n] += t

    def find(self, x: str) -> str:
        root = x
        while self.father[root] != root:
            root = self.father[root]
        while x != root:
            self.father[x], x = root, self.father[x]
        return root

    def union(self, x: str, y: str) -> bool:
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            if self.time[rootX] < self.time[rootY]:
                self.father[rootX] = rootY
            else:
                self.father[rootY] = rootX
            self.cnt -= 1
            return True
        else:
            return False


if __name__ == '__main__':
    N, K = map(int, input().split())
    ufs, names = UnionFindSet(), set()

    for i in range(N):
        name1, name2, time = input().split()
        names.add(name1)
        names.add(name2)
        ufs.add(name1, int(time))
        ufs.add(name2, int(time))
        ufs.union(name1, name2)

    gangs, ans = dict(), list()
    for name in names:
        gang = list()
        head = ufs.find(name)
        if not gangs.get(head, None):
            gangs[head] = list()
        if name not in gangs[head]:
            gangs[head].append((name, ufs.time[name]))
    for k, v in gangs.items():
        if len(v) > 2 and sum([i[1] for i in v]) // 2 > K:
            v = sorted(v, key=lambda x: -x[1])
            ans.append((v[0], len(v)))
    ans = sorted(ans, key=lambda x: x[0][0])
    print(len(ans))
    for item in ans:
        print(item[0][0], item[1])
