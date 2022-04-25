from itertools import combinations


def check(n1: list, n2: list) -> bool:
    if sum(n1) == sum(n2):
        n3 = [i ** 2 for i in n1]
        n4 = [i ** 2 for i in n2]
        if sum(n3) == sum(n4):
            n5 = [i ** 3 for i in n1]
            n6 = [i ** 3 for i in n2]
            if sum(n5) == sum(n6):
                print(f"n1 = {n1}, n2 = {n2}")
                return True
    return False


if __name__ == '__main__':
    nums = [i for i in range(1, 17)]
    for item in combinations(nums, 8):
        if check(list(set(nums) - set(item)), list(item)):
            exit()
