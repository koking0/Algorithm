def check(i: int):
    for it in map(int, list(str(i))):
        if it % 2 == 0:
            return False
    return True

num = 0
while True:
    if num % 2019 == 0 and check(num):
        break
    num += 1
print(num)
