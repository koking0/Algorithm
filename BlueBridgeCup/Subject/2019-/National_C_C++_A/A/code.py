content = []
with open("inc.txt") as fp:
    for line in fp.readlines():
        content.append(list(line.strip()))

ans, dirs = 0, [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
for i in range(len(content)):
    for j in range(len(content[i])):
        ch = content[i][j]
        for dx, dy in dirs:
            x1, y1 = i, j
            while True:
                x1 += dx
                y1 += dy
                x2, y2 = x1, y1

                if x1 < 0 or y1 < 0 or x1 >= len(content) or y1 >= len(content[x1]):
                    break

                while True:
                    x2 += dx
                    y2 += dy
                    if x2 < 0 or y2 < 0 or x2 >= len(content) or y2 >= len(content[x2]):
                        break
                    if content[i][j] < content[x1][y1] < content[x2][y2]:
                        ans += 1
print(ans)
