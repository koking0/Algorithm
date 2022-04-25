class Node:
    def __init__(self, s=None, e=None, c=None):
        self.start = s
        self.end = e
        self.cost = c


def find(x):
    return x if x == pre[x] else pre[x] = find(pre[x])


if __name__ == '__main__':
    n, m = map(int, input().split())
    s, pre = [], [i for i in range(n + 1)]

    for _ in range(m):
        s.append(Node(map(int, input().split())))

    k = m
    for i in range(1, n + 1):
        c = int(input())
        if c != -1:
            s[k].start = 0
            s[k].end = i
            s[k].cost = c
            k += 1

    for i in range(m):
        x = find(s[i].start)
        y = find(s[i].end)
        if x != y:
            pre[x] = y
