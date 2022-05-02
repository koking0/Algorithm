def solve():
    for x in range(2020, 10000):
        for y in range(x + 1, 10000):
            if y ** 2 - x ** 2 == x ** 2 - 2019 ** 2:
                print(f"X = {x}, Y = {y}, X + Y = {x + y}")
                return


if __name__ == '__main__':
    solve()