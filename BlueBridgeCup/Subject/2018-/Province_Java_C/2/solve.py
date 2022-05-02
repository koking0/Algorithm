if __name__ == '__main__':
    for i in range(100, 10000):
        sums = i
        if sums % 5 == 1:
            sums -= (sums // 5 + 1)
            if sums % 5 == 2:
                sums -= (sums // 5 + 2)
                if sums % 5 == 3:
                    sums -= (sums // 5 + 3)
                    if sums % 5 == 4:
                        sums -= (sums // 5 + 4)
                        if sums % 5 == 0:
                            print(i)
                            break
