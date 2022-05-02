if __name__ == '__main__':
    k, p, l = map(int, input().split())
    k = k + 1
    arr = [[0] * 2 for _ in range(k)]
    arr[0][1] = arr[0][0] = 1
    
    i = 1
    while l > 0:
        total = 0
        for j in range(1, p):
            total = (total + arr[(k + i - j) % k][1]) % 20201114
        arr[i][0] = total
        for j in range(p, k):
            total = (total + arr[(k + i - j) % k][0]) % 20201114
        arr[i][1] = total
        l -= 1
        i = (i + 1) % k
        
    i = (k + i - 1) % k
    print(arr[i][1])
