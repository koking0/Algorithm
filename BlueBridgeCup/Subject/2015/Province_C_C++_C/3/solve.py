from itertools import permutations


def solve1():
    """
    三 羊 献 瑞 祥 生 辉 气
    """
    for san in range(10):
        for yang in range(10):
            if yang != san:
                for xian in range(10):
                    if xian != san and xian != yang:
                        for rui in range(10):
                            if rui != san and rui != yang and rui != xian:
                                for xiang in range(10):
                                    if xiang != san and xiang != yang and xiang != xian and xiang != rui:
                                        for sheng in range(10):
                                            if sheng != san and sheng != yang and sheng != xian and sheng != rui and sheng != xiang:
                                                for hui in range(10):
                                                    if hui != san and hui != yang and hui != xian and hui != rui and hui != xiang and hui != sheng:
                                                        for qi in range(10):
                                                            if qi != san and qi != yang and qi != xian and qi != rui and qi != xiang and qi != sheng and qi != hui:
                                                                num1 = int("".join(map(str, [xiang, rui, sheng, hui])))
                                                                num2 = int("".join(map(str, [san, yang, xian, rui])))
                                                                num3 = int("".join(map(str, [san, yang, sheng, rui, qi])))
                                                                if num1 + num2 == num3:
                                                                    print(f"num1 = {num1}, num2 = {num2}, num3 = {num3}")


def solve2():
    for item in permutations(range(10)):
        三, 羊, 献, 瑞, 祥, 生, 辉, 气 = item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]
        num1 = int("".join(map(str, [祥, 瑞, 生, 辉])))
        num2 = int("".join(map(str, [三, 羊, 献, 瑞])))
        num3 = int("".join(map(str, [三, 羊, 生, 瑞, 气])))
        if num1 + num2 == num3:
            print(f"num1 = {num1}, num2 = {num2}, num3 = {num3}")


if __name__ == '__main__':
    solve2()
