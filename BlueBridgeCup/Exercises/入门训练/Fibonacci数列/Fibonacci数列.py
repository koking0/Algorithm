def fibo(n):
    if n == 0 or n == 1:
        return 1
    fn = [0, 1]
    for i in range(n - 1):
        fn[0], fn[1] = fn[1], (fn[0] + fn[1]) % 10007
    return fn[1]


print(fibo(int(input())))
