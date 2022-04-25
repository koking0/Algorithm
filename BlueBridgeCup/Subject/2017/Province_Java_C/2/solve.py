def readFile(file) -> set:
    tmp = set()
    with open(file, 'r') as fp:
        for line in fp.readlines():
            line = line.strip().split()
            for item in line:
                tmp.add(int(item.lstrip().rstrip().replace(',', '')))
    return tmp


if __name__ == '__main__':
    aSet = readFile("A.txt")
    bSet = readFile("B.txt")
    cSet = readFile("C.txt")
    print(len(aSet & bSet - (aSet & bSet & cSet)))
