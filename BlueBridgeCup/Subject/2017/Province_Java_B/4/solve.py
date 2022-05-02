from functools import reduce


def f(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


if __name__ == '__main__':
    s1 = f(8) * 3 ** 8 / 16
    s2 = 3 * f(4) * 3 ** 4
    s3 = 6 * f(4) * 3 ** 4
    print(((s1 + s2 + s3) // 24) // 3)
