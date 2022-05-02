if __name__ == '__main__':
    N, b = map(int, input().split())
    ans = []
    while N:
        remain = N % b
        N = N // b
        ans.append(remain)
    ans.reverse()
    print("Yes" if ans == ans[::-1] else "No")
    print(ans[0], end='')
    ans.pop(0)
    for i in ans:
        print(f" {i}", end='')
