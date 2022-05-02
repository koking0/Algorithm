from itertools import permutations


def check(n: int) -> bool:
    return len(set(list(str(n)))) == 9 and '0' not in str(n)


if __name__ == '__main__':
    nums, ans = ['1', 'B', '3', '4', '5', '6', '7', 'H', '9'], 0
    for item in permutations(nums):
        for i in range(1, len(item)):
            num1 = int(''.join(item[:i]))
            num2 = int(''.join(item[i:]))
            if num2 > num1:
                num = num1 * num2
                if check(num):
                    print(f"{num1} * {num2} = {num}")
                    ans += 1
    print(ans)
