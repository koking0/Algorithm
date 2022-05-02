from math import gcd


if __name__ == "__main__":
    N = int(input())
    A = list()
    for _ in range(N):
        A.append(int(input()))

    x = A[0]
    for a in A[1:]:
        x = gcd(x, a)

    if x > 1:
        print("INF")
    else:
        dp = [[False] * 10007 for _ in range(2)]
        dp[0][0] = True
        for i in range(1, N + 1):
            for j in range(10007):
                if dp[(i - 1) % 2][j]:
                    dp[i % 2][j] = True
                    continue
                r = 1
                while j - r * A[(i - 1) % 2] > -1:
                    if dp[(i - 1) % 2][j - r * A[(i - 1) % 2]]:
                        dp[i % 2][j] = True
                        break
                    r += 1

        ans = 0
        for j in range(1, 10007):
            if not dp[N % 2][j]:
                ans += 1
        print(ans)
