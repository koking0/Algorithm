from itertools import permutations


def check(arr: tuple) -> bool:
    for i in range(len(arr) - 1):
        if arr[i] + 1 == arr[i + 1] or arr[i] - 1 == arr[i + 1]:
            return False
    return True


if __name__ == '__main__':
    books, ans = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0
    for item in permutations(books):
        if check(item):
            ans += 1
    print(ans)
