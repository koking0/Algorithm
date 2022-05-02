import math


def isSquare(n):
    return int(math.sqrt(n)) ** 2 == n

def check(num):
    ans = 0
    for i in range(1, num):
        if isSquare(i) and isSquare(num - i) and i < num - i:
            # print(f'{math.sqrt(i)} ** B + {math.sqrt(num - i)} ** B = {num}')
            ans += 1
    if ans == 12:
        print(num)
        return ans
    else:
        ans = 0

people, count = 1, 1
while count != 12:
    count = check(people)
    people += 1
