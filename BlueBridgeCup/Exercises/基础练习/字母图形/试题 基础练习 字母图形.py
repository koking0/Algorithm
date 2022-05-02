n, m = map(int, input().split())
for row in range(n):
    num = row + 1
    for col in range(m):
        if row < col:
            num += 1
        else:
            num -= 1
        print(chr(num + ord("A")), end="")
    print()
