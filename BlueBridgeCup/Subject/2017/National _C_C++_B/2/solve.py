import sys


def check(x: int, y: int) -> bool:
    for i in range(x - 1):
        for j in range(y - 1):
            if (maps[i][j] + maps[i + 1][j] + maps[i][j + 1] + maps[i + 1][j + 1]) in [0, 4, 8]:
                return False
    return True


def dfs(x: int, y: int):
    if x > rows - 1 or y > cols - 1:
        return

    if x == rows - 1 and y == cols - 1 and check(rows, cols):
        ret = 0
        for i in range(len(maps)):
            for j in range(len(maps[i])):
                if maps[i][j] == 0:
                    return
                ret = ret * 2 + maps[i][j]
        if ret in vis:
            return

        # for item in maps:
        #     print(item)
        # print()

        global ans
        ans += 1
        vis.add(ret)

    if maps[x][y] == 0:
        # 横着铺
        if y + 1 < cols and maps[x][y + 1] == 0:
            for i in [1, 2]:
                maps[x][y] = maps[x][y + 1] = i
                if y == cols - 1:
                    dfs(x + 1, 0)
                else:
                    dfs(x, y + 1)
                maps[x][y] = maps[x][y + 1] = 0

        # 竖着铺
        if x + 1 < rows and maps[x + 1][y] == 0:
            for i in [1, 2]:
                maps[x][y] = maps[x + 1][y] = i
                if y == cols - 1:
                    dfs(x + 1, 0)
                else:
                    dfs(x, y + 1)
                maps[x][y] = maps[x + 1][y] = 0

    if y == cols - 1:
        dfs(x + 1, 0)
    else:
        dfs(x, y + 1)


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    rows, cols, vis, ans = 3, 6, set(), 0
    maps = [[0 for _ in range(cols)] for _ in range(rows)]  # 0 表示还没有贴瓷砖，1 表示黄色瓷砖，2表示橙色瓷砖
    dfs(0, 0)
    print(ans)
