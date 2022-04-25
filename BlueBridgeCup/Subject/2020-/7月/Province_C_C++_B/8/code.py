def dfs(x, y):
    if (x % 2 == 0 and y % 2 == 0) or (x > n or y > m):
        return 0
    if x == n and y == m:
        return 1
    return dfs(x + 1, y) + dfs(x, y + 1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    ans = 0
    print(dfs(1, 1))
