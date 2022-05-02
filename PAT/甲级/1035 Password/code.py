if __name__ == '__main__':
    N, ans = int(input()), []
    for _ in range(N):
        flag = False
        username, password = input().split()
        if '1' in password:
            flag = True
            password = password.replace('1', '@')
        if '0' in password:
            flag = True
            password = password.replace('0', '%')
        if 'l' in password:
            flag = True
            password = password.replace('l', 'L')
        if 'O' in password:
            flag = True
            password = password.replace('O', 'o')
        if flag:
            ans.append((username, password))
    if len(ans):
        print(len(ans))
        for item in ans:
            print(item[0], item[1])
    else:
        if N == 1:
            print("There is 1 account and no account is modified")
        else:
            print(f"There are {N} accounts and no account is modified")
