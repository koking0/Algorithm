def conversion(num: int, base: int):
    ans = []
    while num:
        ans.append(num % base)
        num //= base
    return list(reversed(ans))


if __name__ == '__main__':
    n = int(input())
    maps1 = ["tret", "jan", "feb", "mar", "apr", "may", "jun", "jly", "aug", "sep", "oct", "nov", "dec"]
    maps2 = ["####", "tam", "hel", "maa", "huh", "tou", "kes", "hei", "elo", "syy", "lok", "mer", "jou"]
    for _ in range(n):
        number = input()
        if number.isdigit():
            tmp = conversion(int(number), 13)
            if len(tmp) == 0:
                print("tret")
            elif len(tmp) == 1:
                print(f"{maps1[tmp[0]]}")
            else:
                if tmp[1] != 0:
                    print(f"{maps2[tmp[0]]} {maps1[tmp[1]]}")
                else:
                    print(f"{maps2[tmp[0]]}")
        else:
            number = number.split()
            if len(number) == 1:
                try:
                    print(maps1.index(number[0]))
                except ValueError:
                    print(maps2.index(number[0]) * 13)
            else:
                print(maps2.index(number[0]) * 13 + maps1.index(number[1]))
