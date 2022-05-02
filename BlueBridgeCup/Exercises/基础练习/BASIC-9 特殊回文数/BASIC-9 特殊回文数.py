target = int(input())
for num in range(10000, 1000000):
    if str(num) == str(num)[::-1]:
        sum = 0
        for i in str(num):
            sum += int(i)
        if sum == target:
            print(num)
