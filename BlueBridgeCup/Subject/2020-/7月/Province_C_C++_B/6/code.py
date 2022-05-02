if __name__ == '__main__':
    n = int(input())
    ans = []
    while n:
        ans.append(n)
        n //= 2
    print(" ".join(map(str, ans)))
