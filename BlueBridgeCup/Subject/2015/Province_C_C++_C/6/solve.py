def check(n):
    n2 = n ** 2
    n3 = n ** 3
    tmp = str(n2) + str(n3)
    if len(tmp) == 10 and len(set(tmp)) == 10:
        print(f"num = {n}, n ^ 2 = {n2}, n ^ 3 = {n3}")
        return False
    return True


if __name__ == '__main__':
    num = 0
    while check(num):
        num += 1
