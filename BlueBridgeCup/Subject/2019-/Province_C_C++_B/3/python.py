if __name__ == '__main__':
    a, b, c = 1, 1, 1
    for i in range(3, 20190324):
        a, b, c = b, c, (a + b + c) % 10000
    print(f"第 {i + 1} 项：{c}")
