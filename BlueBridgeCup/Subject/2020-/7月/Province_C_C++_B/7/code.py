if __name__ == '__main__':
    string = input()
    ans = ''
    for i in range(len(string)):
        if i + 1 < len(string) and string[i + 1].isdigit():
            ans += string[i] * int(string[i + 1])
        elif string[i].isdigit():
            continue
        else:
            ans += string[i]
    print(ans)
