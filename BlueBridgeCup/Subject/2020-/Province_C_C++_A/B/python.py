def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


if __name__ == '__main__':
    ans = 0
    for zi in range(1, 2021):
        for mu in range(1, 2021):
            if zi != mu and gcd(zi, mu) == 1:
                ans += 1
    print(ans)
