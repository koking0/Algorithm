from itertools import permutations
from math import sqrt

if __name__ == '__main__':
    nums = [i for i in range(10)]
    for item in permutations(nums):
        num = int("".join(map(str, item)))
        if int(sqrt(num)) ** 2 == num:
            print(num)
