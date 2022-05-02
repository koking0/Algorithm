for num in range(100, 1000):
    sum = 0
    for i in str(num):
        sum += (int(i) ** 3)
    if sum == num:
        print(num)
