def check(num):
    if len(num) < 2:
        return -1
    if len(num) < 3:
        num = "0" + num
    if int(num[-3]) & 1:
        if int(num[-2]) & 1:
            if int(num[-1] & 1):
                return num[:-1]
            else:
                return num[:-1]
        else:
            if int(num[-1] & 1):
                return num
            else:
                return -1
    else:
        if int(num[-2]) & 1:
            if int(num[-1] & 1):
                return num
            else:
                return -1
        else:
        if int(num[-1] & 1):
            return num
        else:
            return -1


if __name__ == '__main__':
    for _ in range(int(input())):
        length = int(input())
        number = input()
        print(check(number))