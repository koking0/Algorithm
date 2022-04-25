from itertools import permutations

if __name__ == '__main__':
    ans, cards = 0, [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for item in permutations(cards):
        sum1 = item[0] + item[1] + item[3] + item[5]
        sum2 = item[0] + item[2] + item[4] + item[8]
        sum3 = item[5] + item[6] + item[7] + item[8]
        if sum1 == sum2 and sum2 == sum3:
            ans += 1
            print(f"{item[0]}\n{item[1]} {item[2]}\n{item[3]}  {item[4]}\n{item[5]} {item[6]} {item[7]} {item[8]}")
    print(ans // 6)
