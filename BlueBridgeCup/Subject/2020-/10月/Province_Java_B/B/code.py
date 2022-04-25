nums = []
with open("2020.txt", 'r') as fp:
    for line in fp.readlines():
        nums.append(list(map(int, list(line.lstrip().rstrip()))))

ans, rows, cols = 0, len(nums), len(nums[0])
for i in range(rows):
    for j in range(cols):
        if nums[i][j] == 2:
            if j + 3 < cols and nums[i][j + 1] == 0 and nums[i][j + 2] == 2 and nums[i][j + 3] == 0:
                ans += 1
            if i + 3 < rows and nums[i + 1][j] == 0 and nums[i + 2][j] == 2 and nums[i + 3][j] == 0:
                ans += 1
            if i + 3 < rows and j + 3 < cols and nums[i + 1][j + 1] == 0 and nums[i + 2][j + 2] == 2 and nums[i + 3][j + 3] == 0:
                ans += 1
print(ans)
