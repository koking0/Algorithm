if __name__ == '__main__':
    ans = 0
    for x in range(-2100, 4100):
        for y in range(-2100, 4100):
            if abs(x - 0) + abs(y - 0) < 2021 or \
                    abs(x - 2020) + abs(y - 11) < 2021 or \
                    abs(x - 11) + abs(y - 14) < 2021 or \
                    abs(x - 2000) + abs(y - 2000) < 2021:
                ans += 1
    print(f"ans = {ans}")
