if __name__ == '__main__':
    n = 123456
    a, b, c, d = 2, 3, 2, 3
    for i in range(n - 1):
        tmp1 = a * c - b * d
        tmp2 = a * d + b * c
        a = tmp1
        b = tmp2
    print(a)
    print()
    print(b)
