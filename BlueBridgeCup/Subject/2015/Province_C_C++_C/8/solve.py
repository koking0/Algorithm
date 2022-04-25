if __name__ == '__main__':
    n = int(input())
    ans = n
    while n > 0:
        n -= 2
        ans += 1
    print(ans - 1)
