class UnionFindSet:
    def __init__(self, n: int):
        self.count = n
        self.father = [x for x in range(n + 2)]

    def find(self, x):
        root = x
        while self.father[root] != root:
            root = self.father[root]
        while root != x:
            self.father[x] = root
            x = self.father[x]
        return root

    def merge(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.rootX = rootY
            self.count -= 1


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        ufs = UnionFindSet(4 * n * n)
        for i in range(n):
            for j in range(n):
                op = grid[i][j]
                index = 4 * (n * i + j)
                
                if op == ' ':
                    ufs.merge(index + 1, index + 2)
                    ufs.merge(index + 2, index + 3)
                    ufs.merge(index + 3, index + 4)
                elif op == '/':
                    ufs.merge(index + 1, index + 2)
                    ufs.merge(index + 3, index + 4)
                elif op == '\\':
                    ufs.merge(index + 1, index + 3)
                    ufs.merge(index + 2, index + 4)

                if j > 0:
                    ufs.merge(index, index + 1)
                if j < n - 1:
                    ufs.merge(index + 4, index + 5)
                if i > 0:
                    ufs.merge(index + 2, index - 4 * n + 3)
                if i < n - 1:
                    ufs.merge(index + 3, index + 4 * n + 2)
        return ufs.count
