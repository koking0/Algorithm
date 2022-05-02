import datetime


if __name__ == '__main__':
    time1 = datetime.datetime.strptime("1921-07-23 12:00:00", "%Y-%m-%d %H:%M:%S")
    print(time1)
    time2 = datetime.datetime.strptime("2020-07-01 12:00:00", "%Y-%m-%d %H:%M:%S")
    print(time2)
    print((time2 - time1).total_seconds() / 60)
