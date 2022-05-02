if __name__ == '__main__':
    ans, n = 0, 100
    for i in range(n):
        ans += (-1) ** i * 4 / (2 * i + 1)
    print(ans)
