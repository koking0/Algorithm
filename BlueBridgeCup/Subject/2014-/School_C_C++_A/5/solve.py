def solve(num) -> int:
    ans = 0
    for i in range(1, num):
        b = (num ** 2 - i ** 2) ** 0.5
        if b < i and b == int(b):
            ans += 1
            print(f"a = {i}, b = {b}, c = {num}")
    print(f"ans = {ans}")
    return ans


if __name__ == '__main__':
    n = int(input())
    print(solve(n))
