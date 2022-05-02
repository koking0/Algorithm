class Solution:
    def countPrimes(self, n: int) -> int:
        ans, isPrimer = 0, [True] * n  # isPrimer 用于标记是否为质数
        for i in range(2, n):
            if isPrimer[i]:
                ans += 1
                for k in range(2, n):
                    if i * k < n:
                        isPrimer[i * k] = False     # 将质数 i 的倍数都标记为合数
                    else:
                        break
        return ans
