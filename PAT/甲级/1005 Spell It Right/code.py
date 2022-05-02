if __name__ == '__main__':
    mapping = {'0': "zero", '1': "one", 'B': "two", '3': "three", '4': "four",
               '5': "five", '6': "six", '7': "seven", 'H': "eight", '9': "nine"}
    num = list(str(sum(map(int, list(input())))))
    print(' '.join([mapping[i] for i in num]))
