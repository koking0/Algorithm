n = int(input())
nums = list(map(int, input().split()))
for _ in range(int(input())):
    l, r, k = map(int, input().split())
    temp = nums[l-1:] if r == len(nums) else nums[l-1: r]
    temp.sort(reverse=True)
    print(temp[k - 1])
