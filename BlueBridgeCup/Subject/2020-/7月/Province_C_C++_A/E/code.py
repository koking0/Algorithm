import math


def check(n):
    for i in list(map(int, list(str(n)))):
        if i not in [0, 1, 4, 9]:
            return False
    if (int(math.sqrt(n)) ** 2) == n:
        # 本身是完全平方数
        for i in list(map(int, list(str(n)))):
            if not ((int(math.sqrt(i)) ** 2) == i):
                return False
        return True
    else:
        return False


if __name__ == '__main__':
    index, num = 0, 0
    while True:
        if check(num):
            index += 1
            print(f'第{ index }个完美平方数是：{ num }')
        if index == 2020:
            break
        num += 1
