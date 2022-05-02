if __name__ == '__main__':
    a, da, b, db = map(list, input().split())
    na = a.count(da[0]) * da
    nb = b.count(db[0]) * db
    if not na:
        na = ['0']
    if not nb:
        nb = ['0']
    print(int(''.join(na)) + int(''.join(nb)))
