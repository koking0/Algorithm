import datetime

if __name__ == '__main__':
    start = datetime.datetime.strptime(input(), "%Y%m%d")
    ans1, ans2 = None, None
    while not ans1 or not ans2:
        start += datetime.timedelta(1)
        if not ans1:
            tmp = start.strftime("%Y%m%d")
            if tmp == tmp[::-1]:
                ans1 = start
        if not ans2:
            tmp = start.strftime("%Y%m%d")
            a, b = tmp[0], tmp[1]
            if tmp == f"{a}{b}{a}{b}{b}{a}{b}{a}":
                ans2 = start
    print(ans1.strftime("%Y%m%d"))
    print(ans2.strftime("%Y%m%d"))
