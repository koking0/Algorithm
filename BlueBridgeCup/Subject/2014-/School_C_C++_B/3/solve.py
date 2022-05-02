if __name__ == '__main__':
    left, right = 2, 3
    while True:
        middle = (left + right) / 2
        if len(str(middle)) > 20:
            break
        print(f"left = {left}, right = {right}, middle = {middle}, middle ** middle = {middle ** middle}")
        if middle ** middle < 10:
            left = middle
        else:
            right = middle
