_ = input()
try:
    print(list(map(int, input().split())).index(int(input())) + 1)
except:
    print(-1)
