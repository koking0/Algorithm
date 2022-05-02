if __name__ == '__main__':
    matrix = []
    with open("./2020.txt", 'r') as fp:
        for line in fp.readlines():
            line = line.strip()
            matrix.append(list(line))

    ans = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'B':
                if j + 3 < len(matrix[i]) \
                        and matrix[i][j + 1] == '0' \
                        and matrix[i][j + 2] == 'B' \
                        and matrix[i][j + 3] == '0':
                    ans += 1
                if i + 3 < len(matrix) \
                        and matrix[i + 1][j] == '0' \
                        and matrix[i + 2][j] == 'B' \
                        and matrix[i + 3][j] == '0':
                    ans += 1
                if i + 3 < len(matrix) \
                        and j + 3 < len(matrix[i]) \
                        and matrix[i + 1][j + 1] == '0' \
                        and matrix[i + 2][j + 2] == 'B' \
                        and matrix[i + 3][j + 3] == '0':
                    ans += 1
    print(ans)
