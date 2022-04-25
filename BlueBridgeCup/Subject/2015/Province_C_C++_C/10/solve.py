from functools import lru_cache


def get_op(num: int) -> int:
    switch = {1: 4, 4: 1, 2: 5, 5: 2, 3: 6, 6: 3}
    return switch.get(num)


@lru_cache(10000)
def dfs(u: int, cnt: int) -> int:
    if cnt == 0:
        return 4
    tmp = 0
    for upper in range(1, 7):
        if not conflict[get_op(u)][upper]:
            tmp = (tmp + dfs(upper, cnt - 1)) % MOD
    return tmp


if __name__ == '__main__':
    ans, MOD = 0, 1e9 + 7
    conflict = [[False] * 7 for _ in range(7)]
    n, m = map(int, input().split())
    for _ in range(m):
        x, y = map(int, input().split())
        conflict[x][y], conflict[y][x] = True, True

    # DFS方法超时
    # for up in range(1, 7):
    #     ans = (ans + 4 * dfs(up, n - 1)) % MOD
    # print(int(ans))

    # DP
    dp = [[0] * 2 for _ in range(7)]
    for i in range(1, 7):
        dp[i][0] = 4

    cur = 1
    for i in range(1, n):  # 计算第 i 个骰子的方案数
        for upper in range(1, 7):  # 第 i 个骰子 upper 朝上
            for up in range(1, 7):  # 第 i - 1 个骰子 up 朝上
                # 如果 i 的下面和 i - 1 的上面不冲突
                if not conflict[get_op(upper)][up]:
                    dp[upper][cur] = (dp[upper][cur] + 4 * dp[up][1 - cur]) % MOD
        cur = 1 - cur
    print(int((sum([dp[i][n - 1] for i in range(7)])) % MOD))
