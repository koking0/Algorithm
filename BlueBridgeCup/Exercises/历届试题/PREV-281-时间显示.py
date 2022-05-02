import datetime

if __name__ == '__main__':
    ans = datetime.datetime(1940, 1, 1, 0, 0, 0) + datetime.timedelta(milliseconds=int(input()))
    print(ans.strftime("%H:%M:%S"))
