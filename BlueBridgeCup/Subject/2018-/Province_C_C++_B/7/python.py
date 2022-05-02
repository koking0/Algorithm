if __name__ == '__main__':
    x, y = map(int, input().split())
    k = max(abs(x), abs(y))
    if x > y:
        print((2 * k) ** 2 + abs(k - x) + abs(k - y))
    else:
        print((2 * k) ** 2 - abs(k - x) - abs(k - y))
