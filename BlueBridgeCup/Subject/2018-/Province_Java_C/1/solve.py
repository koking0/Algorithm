if __name__ == '__main__':
    cash, wage, day = 0, 1, 0
    while cash < 108:
        cash += wage
        wage += 2
        day += 1
    print(f"第 {day} 天，cash = {cash}")
