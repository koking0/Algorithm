def infest(matrix, i, j, rows, cols):
    if i < 0 or i > rows - 1 or j < 0 or j > cols - 1 or matrix[i][j] != 1:
        return
    matrix[i][j] = 2
    infest(matrix, i + 1, j, rows, cols)
    infest(matrix, i - 1, j, rows, cols)
    infest(matrix, i, j + 1, rows, cols)
    infest(matrix, i, j - 1, rows, cols)


def countIslands(matrix):
    if matrix is None or matrix[0] is None:
        return 0

    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                result += 1
                infest(matrix, i, j, len(matrix), len(matrix[0]))

    return result


if __name__ == '__main__':
    m1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0, 1, 1, 1, 0],
          [0, 1, 1, 1, 0, 0, 0, 1, 0],
          [0, 1, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 1, 0, 0],
          [0, 0, 0, 0, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(countIslands(m1))

    m2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 0, 0, 0, 1, 0],
          [0, 1, 1, 0, 0, 0, 1, 1, 0],
          [0, 0, 0, 0, 0, 1, 1, 0, 0],
          [0, 0, 0, 0, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(countIslands(m2))
