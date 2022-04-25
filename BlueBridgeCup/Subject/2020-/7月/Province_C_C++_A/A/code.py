if __name__ == '__main__':
    """
    两分钟 -》 -300
    10000 // 300 = 33
    32 * 300 = 9600
    剩余 10000 - 9600 = 400体力
    一分钟消耗600体力
    一秒钟消耗10体力
    400体力可以消耗40秒
    32 * 120 + 40 = 3880
    """
    n, run, ans = 10000, True, 0
    while n:
        for i in range(60):
            ans += 1
            n -= 10
            if n == 0:
                print(ans)
                exit()
        for i in range(60):
            ans += 1
            n += 5
