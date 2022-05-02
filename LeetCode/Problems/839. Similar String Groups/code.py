from typing import List


class UnionFindSet:
    def __init__(self, n: int):
        self.size = n
        self.father, self.rank = [i for i in range(n)], [1] * n

    def find(self, x: int) -> int:
        root = x
        while self.father[root] != root:
            root = self.father[root]
        while x != root:
            self.father[x], x = root, self.father[x]
        return root

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            xSize, ySize = self.rank[x], self.rank[y]
            rootX, rootY = (rootY, rootX) if xSize < ySize else (rootX, rootY)
            self.father[rootY] = rootX
            self.rank[rootX] += self.rank[rootY]
            self.size -= 1
        return False if rootX == rootY else True


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def similar(x, y) -> bool:
            if x == y:
                return True
            cnt = 0
            for i in range(len(x)):
                if x[i] == y[i]:
                    cnt += 1
            return True if cnt == len(x) - 2 else False

        n = len(strs)
        ufs = UnionFindSet(n)
        for i in range(n):
            for j in range(i + 1, n):
                if similar(strs[i], strs[j]) and ufs.find(i) != ufs.find(j):
                    ufs.union(i, j)
        return ufs.size
