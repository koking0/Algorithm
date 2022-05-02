from typing import List


class UnionFindSet:
    def __init__(self, n: int):
        self.count = n
        self.father, self.size = dict(), dict()
        for i in range(n):
            self.size[i] = 1
            self.father[i] = i

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
            xSize, ySize = self.size[rootX], self.size[rootY]
            rootX, rootY = (rootY, rootX) if xSize < ySize else (rootX, rootY)
            self.size[rootX] += self.size[rootY]
            self.father[rootY] = rootX
            self.count -= 1
        return False if rootX == rootY else True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ans, ufsA, ufsB = 0, UnionFindSet(n), UnionFindSet(n)

        for edge in edges:
            edge[1] -= 1
            edge[2] -= 1

        for weight, start, end in edges:
            if weight == 3:
                if not ufsA.union(start, end):
                    ans += 1
                else:
                    ufsB.union(start, end)

        for weight, start, end in edges:
            if weight == 1:
                if not ufsA.union(start, end):
                    ans += 1
            elif weight == 2:
                if not ufsB.union(start, end):
                    ans += 1
        return -1 if ufsA.count != 1 or ufsB.count != 1 else ans


if __name__ == '__main__':
    s = Solution()
    res = s.maxNumEdgesToRemove(n=4, edges=[[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]])
    print(res)
