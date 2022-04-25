def check(x: int, y: int) -> bool:
    res = 0
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        tmp = list()
        for i in range(7):
            nx, ny = x + i * dx, y + i * dy
            if -1 < nx < n and -1 < ny < n:
                tmp.append(maps[nx][ny])
            else:
                continue
        if ''.join(tmp) == "LANQIAO":
            res += 1
    return res


if __name__ == '__main__':
    n = 100
    maps = list()
    with open("input.txt", 'r') as fp:
        for line in fp.readlines():
            maps.append([])
            for ch in line.strip():
                maps[-1].append(ch)
    # print(maps)

    ans = 0
    for i in range(n):
        for j in range(n):
            ans += check(i, j)
    print(ans)
