def check(num: str) -> bool:
    """
    检查 num 是否把 0~9 的 10 个数字每个用且只用了一次
    """
    num = set(list(num))
    return len(num) == 10


if __name__ == '__main__':
    for i in range(100000):
        i2 = i ** 2
        i3 = i ** 3
        ans = str(i2) + str(i3)
        if check(ans):
            print(i)
            break
