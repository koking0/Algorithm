def process_input():
    global maps
    for _ in range(9):
        maps.append(list(map(int, list(input()))))


def check_map():
    """ check maps valid """
    return True


def print_maps():
    global maps
    for i in maps:
        for j in i:
            print(j, end='')
        print()


def check_index(x, y):
    return -1 < x < 9 and -1 < y < 9


def get_valid_nums(x, y):
    set1 = set(maps[x])
    set2 = set()
    for i in range(9):
        set2.add(maps[i][y])
    set3 = set()
    for i in range(-(x % 3), 3 - x % 3):
        for j in range(-(y % 3), 3 - y % 3):
            set3.add(maps[x + i][y + j])
    return set(range(1, 10)) - set1 - set2 - set3


def dfs(x, y):
    if x == 8 and y == 8 and check_map():
        print_maps()
        return

    if not check_index(x, y):
        return

    if maps[x][y] == 0:
        for num in get_valid_nums(x, y):
            maps[x][y] = num
            dfs(x + 1 if y == 8 else x, y + 1 if y < 8 else 0)
        maps[x][y] = 0
    else:
        dfs(x + 1 if y == 8 else x, y + 1 if y < 8 else 0)


if __name__ == '__main__':
    maps = list()
    process_input()
    dfs(0, 0)
