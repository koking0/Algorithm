if __name__ == '__main__':
    ans = 0
    for num in range(10000, 100000):
        if '4' not in str(num):
            ans += 1
    print(ans)
