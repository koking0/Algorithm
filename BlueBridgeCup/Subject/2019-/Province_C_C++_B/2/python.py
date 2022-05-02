if __name__ == '__main__':
    ans, num = '', 2019
    while num:
        ans += f"{chr(num % 26 + ord('A') - 1)}"
        num //= 26
    print(ans[::-1])
