import math


def count(num: int):
    k, ans = 2, 1
    while k < (num // k):
        p = 1
        while num % k == 0:
            num //= k
            p += 1
        ans *= p
        k += 1
    if num > 1:
        ans *= 2
    return ans


if __name__ == '__main__':
    n = math.factorial(100)
    print(f"100! = {n}")
    print(f"约数个数 = {count(n)}")
