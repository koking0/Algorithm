from sys import maxsize


def dfs(node):
    if dp[node] != -1:
        return
    
    # 初始化为0，开始搜索
    min_val = maxsize
    for item in cross_dict.get(node, []):
        a, b = item
        dfs(a)
        dfs(b)
        # 得到作物的最短时间 = A, B之间成熟的较大值 + 获得A. B两种作物所需要的时间
        min_val = min(min_val, max(planting_time[a - 1], planting_time[b - 1]) + max(dp[a], dp[b]))
    
    if min_val != maxsize:
        dp[node] = min_val


if __name__ == '__main__':
    # 处理输入数据
    N, M, K, T = map(int, input().split())
    dp = [-1] * (N + 1)  # dp[i]表示得到作物i的最短时间，全部初始化为-1
    planting_time = list(map(int, input().split()))
    for k in map(int, input().split()):
        dp[k] = 0
    cross_dict = dict()
    for _ in range(K):
        A, B, C = map(int, input().split())
        if not cross_dict.get(C, None):
            cross_dict[C] = []
        cross_dict[C].append((A, B))
    
    dfs(T)  # 以目标作物为根节点进行DFS，先搜索到底部，再自底向上更新
    print(dp[T])
