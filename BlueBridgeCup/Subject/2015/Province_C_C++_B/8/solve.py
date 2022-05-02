if __name__ == '__main__':
    idx, x, y = 1, 0, 0  # 表示当前到达的楼号和坐标
    left_to_right = True
    w, m, n = map(int, input().split())
    mx, my, nx, ny = 0, 0, 0, 0
    while idx < max(m, n) + 1:
        if idx == m:  # 记录 m 号楼的坐标
            mx, my = x, y
        if idx == n:  # 记录 n 号楼的坐标
            nx, ny = x, y

        y = y + 1 if left_to_right else y - 1
        if idx % w == 0:
            x += 1
            left_to_right = not left_to_right
            y = y + 1 if left_to_right else y - 1

        idx += 1
    print(abs(mx - nx) + abs(my - ny))
