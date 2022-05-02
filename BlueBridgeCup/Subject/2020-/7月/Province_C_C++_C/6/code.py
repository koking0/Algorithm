if __name__ == '__main__':
    string = input()
    uppers, lowers, numbers = 0, 0, 0
    for i in string:
        if i.isupper():
            uppers += 1
        elif i.islower():
            lowers += 1
        elif i.isdigit():
            numbers += 1
    print(uppers, lowers, numbers)
