def EulerSieve(n: int) -> list:
    vis, res = [False] * (n + 1), []
    for i in range(2, n + 1):
        if not vis[i]:
            res.append(i)
        for prime in res:
            if i * prime > n:
                break
            vis[i * prime] = True
            if i % prime == 0:
                break
    return res


if __name__ == '__main__':
    length, ans = 10000, []
    primers = EulerSieve(length)
    for tolerance in range(1, 1000):
        for i in range(len(primers)):
            ans.append(primers[i])
            for j in range(i + 1, len(primers)):
                if primers[j] - ans[-1] == tolerance:
                    ans.append(primers[j])
                elif primers[j] - ans[-1] > tolerance:
                    break

                if len(ans) > 9:
                    print(f"ans = {ans}, tolerance = {tolerance}")
                    exit()
            ans.clear()
