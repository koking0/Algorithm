if __name__ == '__main__':
    num, ans = 78120, 0
    for i in range(1, num + 1):
        if num % i == 0:
            ans += 1
    print(ans)
