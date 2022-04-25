if __name__ == '__main__':
    floor, ans = 0, 0
    requestList = list(map(int, input().split()))
    requestList.pop(0)
    for request in requestList:
        if request > floor:
            ans += 6 * (request - floor)
        else:
            ans += 4 * (floor - request)
        ans += 5
        floor = request
    print(ans)
