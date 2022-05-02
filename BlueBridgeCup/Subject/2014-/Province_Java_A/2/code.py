flag, ans = 1, 0
for i in range(100):
    ans += flag * (1 / (2 * i + 1))
    flag *= -1
print(4 * ans)
