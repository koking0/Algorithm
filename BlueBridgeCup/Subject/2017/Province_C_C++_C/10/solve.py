from math import ceil


def attach(i, W, H):
    if W + w[i] > M:
        H = max(H, int(ceil(1.0 * h[i] * (M - W) / w[i])))
    else:
        H = max(H, h[i])
    W = min(M, W + w[i])
    return W, H


def calc(i, W, H):
    while i < N and W < M:
        W, H = attach(i, W, H)
        i += 1
    return H + t[i]


if __name__ == '__main__':
    M, N = map(int, input().split())
    maxn = 100000
    w = [0 for _ in range(maxn)]
    h = [0 for _ in range(maxn)]
    t = [0 for _ in range(maxn)]
    for i in range(N):
        w[i], h[i] = map(int, input().split())
    for i in range(N - 1, -1, -1):
        t[i] = calc(i, 0, 0)
    res = t[0]
    pre_h = 0
    W = 0
    H = 0
    for i in range(N):
        tmp = calc(i + 1, W, H)
        res = min(res, pre_h + tmp)
        attach(i, W, H)
        if W == M:
            pre_h += H
            W = 0
            H = 0
    print(res)
