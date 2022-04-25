class UnionFindSet:
    def __init__(self, n: int):
        self.cnt = n
        self.father = [i for i in range(n)]

    def find(self, x: int) -> int:
        root = x
        while self.father[root] != root:
            root = self.father[root]
        return root

    def union(self, x: int, y: int) -> None:
        if self.find(x) != self.find(y):
            self.father[x] = y
            self.cnt -= 1


def check(n):
    ufs = UnionFindSet(len(n))
    flags = []
    for i in range(len(n)):
        if n[i] == 1:
            flags.append(i)
    for i in range(len(flags) - 1):
        if flags[i + 1] - flags[i] == 1:
            ufs.union(flags[i + 1], flags[i])
        if 0 in flags and 5 in flags:
            ufs.union(0, 5)
        if 6 in flags:
            if flags[i] == 1 or flags[i] == 2 or flags[i] == 4 or flags[i] == 5:
                ufs.union(6, flags[i])
    return (ufs.cnt - n.count(0)) == 1


def dfs(n: list, idx: int, flag: int):
    if idx == 7:
        if check(n):
            ans.add("".join(list(map(str, n))))
        return

    n[idx] = flag
    dfs(n, idx + 1, 0)
    dfs(n, idx + 1, 1)


if __name__ == '__main__':
    ans = set()
    nums = [0, 0, 0, 0, 0, 0, 0]
    dfs(nums, 0, 1)
    dfs(nums, 0, 0)
    for item in ans:
        print(item)
    print(len(ans))
