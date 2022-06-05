class UnionFindSet:
    def __init__(self, n: int):
        self.count = n
        self.father, self.size = [i for i in range(n)], [1] * n

    def find(self, x: int) -> int:
        root = x
        while self.father[root] != root:
            root = self.father[root]
        while x != root:
            self.father[x], x = root, self.father[x]
        return root

    def isSameSet(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            xSize, ySize = self.size[rootX], self.size[rootY]
            big, small = (rootY, rootX) if xSize < ySize else (rootX, rootY)
            self.size[big] += self.size[small]
            self.father[small] = big
            self.count -= 1
        return False if rootX == rootY else True
