maps = [
    ['U', 'D', 'D', 'L', 'U', 'U', 'L', 'R', 'U', 'L'],
    ['U', 'U', 'R', 'L', 'L', 'L', 'R', 'R', 'R', 'U'],
    ['R', 'R', 'U', 'U', 'R', 'L', 'D', 'L', 'R', 'D'],
    ['R', 'U', 'D', 'D', 'D', 'D', 'U', 'U', 'U', 'U'],
    ['U', 'R', 'U', 'D', 'L', 'L', 'R', 'R', 'U', 'U'],
    ['D', 'U', 'R', 'L', 'R', 'L', 'D', 'L', 'R', 'L'],
    ['U', 'L', 'L', 'U', 'R', 'L', 'L', 'R', 'D', 'U'],
    ['R', 'D', 'L', 'U', 'L', 'L', 'R', 'D', 'D', 'D'],
    ['U', 'U', 'D', 'D', 'U', 'D', 'U', 'D', 'L', 'L'],
    ['U', 'L', 'R', 'D', 'L', 'U', 'U', 'R', 'R', 'R'],
]


def dfs(x: int, y: int):
    if x < 0 or x > rows - 1 or y < 0 or y > cols - 1:
        return True
    if visited[x][y]:
        return False

    visited[x][y] = True
    if maps[x][y] == 'U':
        return dfs(x - 1, y)
    if maps[x][y] == 'D':
        return dfs(x + 1, y)
    if maps[x][y] == 'L':
        return dfs(x, y - 1)
    if maps[x][y] == 'R':
        return dfs(x, y + 1)


if __name__ == '__main__':
    rows, cols, ans = len(maps), len(maps[0]), 0
    for i in range(rows):
        for j in range(cols):
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            if dfs(i, j):
                ans += 1
    print(ans)
