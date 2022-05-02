from itertools import combinations


class UnionFindSet:
    def __init__(self, n: int):
        self.count = n
        self.father, self.size = [i for i in range(n)], [1] * n

    def find(self, x: int):
        root = x
        while self.father[root] != root:
            root = self.father[root]
        while x != root:
            self.father[x], x = root, self.father[x]
        return root

    def same(self, x: int, y: int):
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            xSize, ySize = self.size[x], self.size[y]
            rootX, rootY = (rootY, rootX) if xSize < ySize else (rootX, rootY)
            self.father[rootY] = rootX
            self.size[rootX] += self.size[rootY]
            self.count -= 1
        return False if rootX == rootY else True


ans, chs = 0, [0, 1, 2, 3, 4, 5, 6]
for i in range(1, len(chs) + 1):
    for item in (combinations(chs, i)):
        n = len(item)
        ufs = UnionFindSet(n)
        for j in range(n):
            for k in range(j + 1, n):
                if abs(item[j] - item[k]) == 1 or \
                        (item[j] == 0 and item[k] == 5) or \
                        (item[j] == 1 and item[k] == 6) or \
                        (item[j] == 2 and item[k] == 6) or \
                        (item[j] == 4 and item[k] == 6):
                    ufs.union(j, k)
        ans += 1 if ufs.count == 1 else 0
print(ans)
