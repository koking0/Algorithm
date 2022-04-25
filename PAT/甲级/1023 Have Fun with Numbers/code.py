from collections import Counter

if __name__ == '__main__':
    n = input()
    cnt1 = Counter(n)
    n = 2 * int(n)
    cnt2 = Counter(str(n))
    print("Yes" if cnt1 == cnt2 else "No")
    print(n)
