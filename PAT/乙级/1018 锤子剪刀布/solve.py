from collections import Counter


def check(c1, c2) -> int:
    """1 - Win, B - Draw, 3 - Lose"""
    if c1 == c2:
        return 2
    if c1 == 'C':
        if c2 == 'J':
            return 1
        if c2 == 'B':
            return 3
    if c1 == 'J':
        if c2 == 'B':
            return 1
        if c2 == 'C':
            return 3
    if c1 == 'B':
        if c2 == 'C':
            return 1
        if c2 == 'J':
            return 3


if __name__ == '__main__':
    N = int(input())
    A, B = [], []
    aWin = aDraw = aLose = 0
    bWin = bDraw = bLose = 0
    for _ in range(N):
        a, b = input().split()
        flag = check(a, b)
        if flag == 1:
            aWin += 1
            bLose += 1
            A.append(a)
        elif flag == 2:
            aDraw += 1
            bDraw += 1
        elif flag == 3:
            aLose += 1
            bWin += 1
            B.append(b)
    print(aWin, aDraw, aLose)
    print(bWin, bDraw, bLose)
    A.sort()
    B.sort()
    print(max(A, key=A.count), max(B, key=B.count))
