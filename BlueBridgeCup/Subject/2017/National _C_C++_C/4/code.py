def Qpow(a, b, mod):
    res = 1
    while b:
        if b & 1:
            res = res * a % mod
        a = a * a % mod
        b >>= 1
    return res

a, b, n = list(map(int, input().split()))
mod = b * 1000
res = Qpow(10, n + 2, mod)
tem = (a % mod * res % mod) % mod
print(str(int(tem / b)).ljust(3, '0'))
