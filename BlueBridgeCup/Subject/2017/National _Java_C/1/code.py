if __name__ == '__main__':
    ans = 0
    for i in range(1, 1001):
        ans += sum(map(int, list(str(i))))
    print(ans)
