content = []
with open("inc.txt", 'r') as fp:
    for line in fp.readlines():
        content.append(list(line.strip()))

ans, dirs = 0, [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
for i in range(len(content)):
    for j in range(len(content[i])):
        ch = content[i][j]
        for dx, dy in dirs:
            x, y = i, j
            while True:
                x += dx
                y += dy

                if x < 0 or y < 0 or x > len(content) - 1 or y > len(content[x]) - 1:
                    break

                if content[x][y] > ch:
                    ans += 1
print(ans)
