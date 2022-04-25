from math import sqrt


def isPrime(num: int):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    while True:
        line = input()
        if line[0] == '-':
            break
        N, D = map(int, line.split())

        if not isPrime(N):
            print("No")
            continue

        dn = []
        if N == 0:
            dn.append(0)
        else:
            while N != 0:
                remain = N % D
                N = N // D
                dn.append(remain)
        N = int("".join(map(str, dn)), D)

        print("Yes" if isPrime(N) else "No")
