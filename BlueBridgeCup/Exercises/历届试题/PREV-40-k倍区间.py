if __name__ == '__main__':
    N, K = map(int, input().split())
    nums = []
    for _ in range(N):
        nums.append(int(input()))
    # print(nums)

    ans = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if not sum(nums[i: j + 1]) % K:
                # print(nums[i: j + 1])
                ans += 1
    print(ans)
