def dfs(id: int, num: int):
    global res
    if num >= res:
        return

    if id > n:
        res = num
        return

    for room in rooms:
        for p in room:
            if relationship[id][p]:
                break
        else:
            room.append(id)
            dfs(id + 1, num)

    rooms.append([id])
    dfs(id + 1, num + 1)


if __name__ == '__main__':
    res = n = int(input())
    m = int(input())
    rooms, relationship = [], [[False for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(m):
        a, b = map(int, input().split())
        relationship[a][b] = True
        relationship[b][a] = True
    dfs(1, 0)
    print(res)
