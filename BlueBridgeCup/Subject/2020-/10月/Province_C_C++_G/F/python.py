if __name__ == '__main__':
    nums = [int(input()) for _ in range(int(input()))]
    print(f"{max(nums)}\n{min(nums)}\n{(sum(nums) / len(nums)):.2f}")
