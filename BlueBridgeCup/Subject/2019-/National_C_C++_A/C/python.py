def get_n(factor_cnt):
    x = factor_cnt
    power = []
    i = 0
    while factor_cnt > 1:
        if factor_cnt % p[i] == 0:
            power.append(p[i])
            factor_cnt = factor_cnt // p[i]
        else:
            i += 1
        
        if i == (len(p) - 1) and factor_cnt != 1:
            power.append(factor_cnt)
            break
    
    n = 1
    power.reverse()
    for j in range(len(power)):
        n *= pow(p[j], power[j] - 1)
    print(x, n)
    return n


if __name__ == '__main__':
    total = 0
    p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 27, 29, 31]
    for m in range(1, 61):  # 求因子数为1——60的最小整数
        if m == 1:
            total += 1
            print(1, 1)
        else:
            total += get_n(m)
    print(total)
