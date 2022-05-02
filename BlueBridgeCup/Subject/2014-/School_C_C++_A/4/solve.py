from itertools import permutations


def check(l) -> bool:
    for i in range(1, 8):
        idx = l.index(i)
        idx = l.index(i, idx + 1) - idx - 1
        if idx != i:
            return False
    return True


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7]
    print(check([1, 7, 1, 2, 6, 4, 2, 5, 3, 7, 4, 6, 3, 5]))
    for item in permutations(nums):
        if check([7, 4] + list(item)):
            print([7, 4] + list(item))
            break
