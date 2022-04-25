class UnionFindSet:
    def __init__(self, n: int) -> None:
        self.cnt = n
        self.father, self.size = [i for i in range(n)], [1] * n

    def find(self, x: int) -> int:
        root = x
        while self.father[root] != root:
            root = self.father[root]
        return root

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, soldier: int, general: int) -> None:
        self.father[soldier] = general


def dfs(x):
    print(f"x = {x}, rank = {rank}")
    if x == n:
        if len(rank) > 1:
            global ans
            ans += 1
        return

    if ufs.find(x) not in rank:
        rank.add(x)
        dfs(x + 1)
        rank.remove(x)
    dfs(x + 1)


if __name__ == '__main__':
    n = int(input())
    persons = list(map(int, input().split(' ')))
    ufs = UnionFindSet(n)
    for i in range(n - 1):
        ufs.union(i + 1, persons[i] - 1)

    ans, rank = 0, set()
    for i in range(n):
        dfs(i)
        print()
    print(ans + n)
