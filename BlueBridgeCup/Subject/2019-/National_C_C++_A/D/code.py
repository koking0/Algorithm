def count(n: int):
    cnt = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt += 1 if i * i == n else 2
    return cnt


ans, num = [1], 0
while len(ans) < 60:
    num += 2
    if count(num) == len(ans) + 1:
        print(num, ans, len(ans))
        ans.append(num)
print(ans)
print(sum(ans))
