from typing import List


class UnionFindSet:
    def __init__(self, n):
        self.n = n
        self.less = 0 # 表示多余的线缆
        self.father = dict()
        for i in range(n):
            self.father[i] = i

    def find(self, x):
        root = x
        while self.father[root] != root:
            root = self.father[root]
        while root != x:
            self.father[x] = root
            x = self.father[x]
        return root

    def merge(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            self.father[rootX] = rootY
            self.n -= 1
        else:
            self.less += 1

    def isSet(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ufs = UnionFindSet(n)
        for item in connections:
            ufs.merge(item[0], item[1])
        num = ufs.n - 1 # 剩余没有连接的计算机
        return num if num < ufs.less + 1 else -1


if __name__ == "__main__":
    s = Solution()
    print(s.makeConnected(4, [[0,1],[0,2],[1,2]]))
