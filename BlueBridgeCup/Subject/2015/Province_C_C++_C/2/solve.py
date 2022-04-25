if __name__ == '__main__':
    ans = 0
    for i in range(1, 10001):
        if str(i) in str(i ** 3)[-len(str(i)):]:
            ans += 1
            print(f"num = {i}, num ^ 3 = {i ** 3}")
    print(ans)
