n = int(input())
matrix = []
for row in range(n):
    matrix.append([0] * n)
    matrix[row][0] = 1
    for col in range(1, n):
        if row == 0:
            continue
        matrix[row][col] = matrix[row - 1][col - 1] + matrix[row - 1][col]
for i in range(n):
    for j in range(n):
        if matrix[i][j]:
            print(matrix[i][j], end=" ")
    print()
