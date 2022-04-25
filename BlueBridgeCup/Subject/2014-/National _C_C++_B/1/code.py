if __name__ == '__main__':
    start = 2000
    for i in range(start, 2014):
        if sum(list(map(int, list(str(i))))) == 2014 - i:
            print(i)
