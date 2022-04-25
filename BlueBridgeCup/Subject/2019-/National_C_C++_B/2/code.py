def EulerSieve(n: int):
    filter, primers = [False for _ in range(n + 1)], []
    for i in range(2, n + 1):
        if not filter[i]:
            primers.append(i)
        for prime in primers:
            if i * prime > n:
                break
            filter[i * prime] = True
            if i % prime == 0:
                break
    return primers


def solve():
    pass


if __name__ == '__main__':
    # solve()
    print(EulerSieve(100))

