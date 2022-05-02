if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = list(map(int, input().split(' ')))
    if m == 0:
        print(sum(nums))
    else:
        ans = 0
        nums.sort()
        for i in range(1, n + m):
            ans += abs(nums[i])
        ans += abs(nums[0] - nums[-1])
        print(ans)
