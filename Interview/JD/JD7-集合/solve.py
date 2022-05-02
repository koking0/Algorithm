if __name__ == '__main__':
    n, m = map(int, input().split())
    set_n = list(map(int, input().split()))
    set_m = list(map(int, input().split()))
    ans = list(set(set_n)) + list(set(set_m))
    ans.sort()
    for i in range(len(ans)):
        if i == 0:
            print(ans[i], end='')
        else:
            print(f" {ans[i]}", end='')
