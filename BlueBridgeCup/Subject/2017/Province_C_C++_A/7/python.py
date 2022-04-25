def dfs():
    global pos
    res, tmp = 0, 0
    while pos < len(s):
        if s[pos] == '(':
            pos += 1
            tmp += dfs()
        elif s[pos] == ')':
            pos += 1
            res = max(res, tmp)
            return res
        elif s[pos] == 'x':
            pos += 1
            tmp += 1
        elif s[pos] == '|':
            pos += 1
            res = max(res, tmp)
            tmp = 0
    res = max(res, tmp)
    return res


if __name__ == '__main__':
    pos = 0
    s = input().strip()
    print(dfs())
