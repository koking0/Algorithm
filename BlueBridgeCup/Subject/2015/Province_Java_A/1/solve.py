if __name__ == '__main__':
    ans, num = 0, 1543
    while num:
        if num % 2:
            print(f"num = {num}, throw 1.")
            num -= 1
            ans += 1
        num //= 2
    print(ans)
