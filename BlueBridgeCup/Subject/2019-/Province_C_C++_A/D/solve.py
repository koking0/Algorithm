from collections import deque


if __name__ == '__main__':
    maze, ans = [], None
    with open("./maze.txt", 'r') as fp:
        for line in fp.readlines():
            maze.append(list(map(int, list(line.strip()))))
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]

    queue = deque()
    queue.append((0, 0, ''))
    while queue:
        x, y, path = queue.popleft()
        if x == rows - 1 and y == cols - 1:
            print(path)
            break

        orientations = ['L', 'D', 'R', 'U']
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        for idx, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if -1 < nx < rows and -1 < ny < cols and maze[nx][ny] == 0 and not visited[nx][ny]:
                queue.append((nx, ny, path + orientations[idx]))
                visited[x][y] = True
