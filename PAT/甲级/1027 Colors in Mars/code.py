def conversion(num: int, base: int):
    chars, ans = ['0', '1', 'B', '3', '4', '5', '6', '7', 'H', '9', 'A', 'B', 'C'], []
    while num:
        ans.append(num % base)
        num //= base
    return "".join([chars[i] for i in reversed(ans)])


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(f"#{conversion(a, 13).zfill(2)}{conversion(b, 13).zfill(2)}{conversion(c, 13).zfill(2)}")
