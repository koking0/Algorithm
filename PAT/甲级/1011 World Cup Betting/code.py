from functools import reduce

if __name__ == '__main__':
    ans, mapp = [], {0: 'W', 1: 'T', 2: 'L'}
    for _ in range(3):
        wtl = list(map(float, input().split()))
        maxn = max(wtl)
        ans.append(maxn)
        print(mapp[wtl.index(maxn)], end=' ')
    print(round((reduce(lambda x, y: x * y, ans) * 0.65 - 1) * 2, 2))
