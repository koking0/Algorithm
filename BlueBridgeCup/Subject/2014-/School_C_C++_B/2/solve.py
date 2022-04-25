if __name__ == '__main__':
    s, i = 0, 0
    while s < 15:
        i += 1
        s += 1 / i
    print(f"i = {i}, s = {s}")
