def dfs(num, minn, maxn):
    if num < 0:
        return
    if num == 0:
        global ans
        ans += 1
        return
    for i in range(minn, maxn + 1):
        dfs(num - i ** 2, minn + 1, maxn)

ans = 0
dfs(num=2019, minn=0, maxn=45)
print(ans)
