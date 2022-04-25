import copy


def spread(num: int):
    x, y = int(num / 10000), int(num % 10000)
    mapping[x][y] = True
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if not mapping[nx][ny]:
            set2.add(nx * 10000 + ny)


if __name__ == '__main__':
    mapping = [[False for _ in range(10000)] for _ in range(10000)]
    set1, set2 = set(), set()
    set1.add(50005000)
    set1.add(70205011)
    set1.add(50115014)
    set1.add(70007000)

    for _ in range(2020):
        for item in set1:
            spread(item)
        set1.clear()
        set1 = copy.deepcopy(set2)
        set2.clear()

    for i in set1:
        mapping[int(i / 10000)][int(i % 10000)] = True

    ans = 0
    for i in mapping:
        ans += i.count(True)
    print(ans)
