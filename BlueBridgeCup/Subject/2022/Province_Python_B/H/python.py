if __name__ == '__main__':
    N, M = map(int, input().split())
    up_list = []
    for _ in range(N):
        A, B = map(int, input().split())
        up_list.append([A, B, A])
    
    ans = 0
    for _ in range(M):
        up_list.sort(key=lambda x: x[2])
        if up_list[-1][-1] > 0:
            ans += up_list[-1][-1]
            up_list[-1][2] -= up_list[-1][1]
    print(ans)
