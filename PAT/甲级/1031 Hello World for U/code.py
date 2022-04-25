if __name__ == '__main__':
    string = input()
    N = len(string)
    n1 = (N + 2) // 3
    n2 = N - n1 * 2
    for i in range(n1 - 1):
        print(f"{string[i]}{' ' * n2}{string[N - i - 1]}")
    print(string[n1 - 1:n1 + n2 + 1])
