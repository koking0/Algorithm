import itertools

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
for item in itertools.combinations(nums, 8):
    a = list(item)
    b = list(set(nums) ^ set(item))
    if sum(a) == sum(b):
        if sum([x ** 2 for x in a]) == sum([x ** 2 for x in b]):
            if sum([x ** 3 for x in a]) == sum([x ** 3 for x in b]):
                print(a, b)
