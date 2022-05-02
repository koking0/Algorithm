n = int(input())
n1, n2 = 0, 0
for i in range(n):
    score = int(input())
    if score >= 85:
        n1 += 1
    if score >= 60:
        n2 += 1
print(f"{round(100 * n2 / n)}%")
print(f"{round(100 * n1 / n)}%")
