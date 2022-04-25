def isPrimeNumber(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    m, n = 0, int(input())
    for i in range(4, n, 2):
        for j in range(2, int(i / 2)):
            if isPrimeNumber(j) and isPrimeNumber(i - j):
                m = max(m, j)
                break
    print(m)
