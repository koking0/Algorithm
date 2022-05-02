if __name__ == '__main__':
    n = int(input())
    while n != 0:
        while True:
            pop_list = list(map(int, input().split(' ')))
            if pop_list[0] == 0:
                break
            idx, stack = 0, []
            for i in range(1, n + 1):
                stack.append(i)
                while stack and stack[-1] == pop_list[idx]:
                    idx += 1
                    stack.pop()
            if idx == n:
                print("Yes")
            else:
                print("No")
        print()
        n = int(input())
