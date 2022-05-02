if __name__ == '__main__':
    left, right = 2, 3
    while len(str(left)) < 19:
        middle = (left + right) / 2
        if middle ** middle < 10:
            left = middle
        else:
            right = middle
        print(f"{middle} ** {middle} = {middle ** middle}")
