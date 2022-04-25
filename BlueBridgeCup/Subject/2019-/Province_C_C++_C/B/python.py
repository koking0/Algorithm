if __name__ == '__main__':
    a, b, ans = 2019, 324, 0
    while a != b:
        ans += 1
        if a > b:
            a -= b
            print(f"切一个 {b} * {b} 的正方形")
        elif a < b:
            b -= a
            print(f"切一个 {a} * {a} 的正方形")
    else:
        print(f"剩一个 {a} * {a} 的正方形")
        ans += 1
    print(f"ans = {ans}")
