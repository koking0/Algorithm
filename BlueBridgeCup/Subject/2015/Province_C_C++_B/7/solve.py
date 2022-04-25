def dfs(cnt, idx):
    """
    cnt: 手里有的牌数
    idx: 当前来到牌型
    """
    if cnt > 13 or idx > 13:
        return
    if cnt == 13 and idx == 13:
        global ans
        ans += 1
        return
    for i in range(5):
        dfs(cnt + i, idx + 1)


if __name__ == '__main__':
    ans = 0
    dfs(0, 0)
    print(ans)
