if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    idx, ans = 0, 0
    while sum(A):
        while idx < N:
            if A[idx]:
                is_k = True
                for j in range(idx, idx + K):
                    if j < N and not A[j]:
                        is_k = False
                        break
                if is_k:
                    for j in range(idx, idx + K):
                        if j < N:
                            A[j] -= 1
                else:
                    A[idx] -= 1
                ans += 1
            else:
                idx += 1
    print(ans)
