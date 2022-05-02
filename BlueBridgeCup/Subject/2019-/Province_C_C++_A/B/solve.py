if __name__ == '__main__':
    a, b, c = 1, 1, 1
    for _ in range(20190324 - 3):
        a, b, c = b, c, (a + b + c) % 100000
    print(c)
