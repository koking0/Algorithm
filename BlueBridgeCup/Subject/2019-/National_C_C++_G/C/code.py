import sys
import datetime


def getPTrainList(p: int):
    ans = []
    for it in trip[1:]:
        if it[1] == places[p] and not vis[places.index(it[2])]:
            ans.append(it)
    return ans


def isAll():
    for i in vis:
        if not i:
            return False
    return True


def dfs(p, minute, t):
    print(places[p], minute, t)
    if p == 0 and minute > 0:
        global minn
        if minn > minute:
            minn = minute
        return

    # 如果不是北京，至少休息一天
    if p:
        minute += 1440

    pTrainList = getPTrainList(p)
    for train in pTrainList:
        if train[2] == "北京":
            vis[0] = True
            if not isAll():
                vis[0] = False
                continue
            vis[0] = False

        ti = minute
        if train[3] > ti:
            ti += train[3] - t + train[4] - train[3]
        else:
            ti += train[3] - t + 1440 + train[4] - train[3]

        vis[places.index(train[2])] = True
        dfs(places.index(train[2]), ti, train[4])
        vis[places.index(train[2])] = False
    

trip = []
with open("trip.txt", 'r') as fp:
    for line in fp.readlines():
        trip.append(line.split())

for line in trip[1:]:
    tmp = line[3].split(':')
    line[3] = int(tmp[0]) * 60 + int(tmp[1])
    tmp = line[4].split(':')
    line[4] = int(tmp[0]) * 60 + int(tmp[1])

places = ["北京", "上海", "广州", "长沙", "西安", "杭州", "济南", "成都", "南京", "昆明", "郑州", "天津", "太原", "武汉", "重庆", "南昌", "长春", "沈阳", "贵阳", "福州"]
vis, minn = [False for _ in range(len(places))], sys.maxsize

time = 12 * 60
dfs(0, 0, time)
print(minn)
