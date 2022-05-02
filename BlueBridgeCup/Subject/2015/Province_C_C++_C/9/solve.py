if __name__ == '__main__':
    m, n = map(int, input().split())
    width = m + n - 1
    mapping = [['.' for _ in range(width)] for _ in range(n)]
    for i in range(n):
        mapping[i][i] = '*'
        mapping[i][i + 1] = '*'
        mapping[i][i + 2] = '*'
        mapping[i][width - i - 1] = '*'
        mapping[i][width - i - 2] = '*'
        mapping[i][width - i - 3] = '*'
    for item in mapping:
        for char in item:
            print(char, end='')
        print()
