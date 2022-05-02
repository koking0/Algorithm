from math import sqrt


def getNum(first: float, second: float) -> int:
    cnt = 0
    for i in range(int(first), int(second) + 1):
        cnt += 1
    if first - int(first) > 0:
        cnt -= 1
    return cnt


if __name__ == '__main__':
    N, L, R = map(int, input().split())
    first, second = sqrt(L), sqrt(R)
    print(R - L + 1 - getNum(first, second))
