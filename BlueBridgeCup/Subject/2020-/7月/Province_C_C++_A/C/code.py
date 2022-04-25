def dfs(index, num):
    if index > len(masks) - 1:
        global minn
        minn = min(minn, abs(sum(masks) - 2 * num))
        return
    dfs(index + 1, num)
    dfs(index + 1, num + masks[index])


if __name__ == '__main__':
    masks = [9090400, 8499400, 5926800, 8547000, 4958200, 4422600, 5751200, 4175600, 6309600, 5865200, 6604400, 4635000,
             10663400, 8087200, 4554000]
    minn = sum(masks)
    dfs(0, 0)
    print(minn)
