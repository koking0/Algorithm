def solve(string):
    for _ in range(2 ** 64):
        if string == "":
            print("EMPTY")
            return
        
        keep_list = [1] * len(string)
        for i in range(len(string)):
            if i > 0 and i + 1 < len(string) and string[i] == string[i - 1] and string[i] != string[i + 1]:
                keep_list[i] = 0
                keep_list[i + 1] = 0
            if i > 0 and i + 1 < len(string) and string[i] != string[i - 1] and string[i] == string[i + 1]:
                keep_list[i] = 0
                keep_list[i - 1] = 0
        if sum(keep_list) == len(string):
            print(string)
            return
      
        new_string = ""
        for i in range(len(string)):
            new_string += string[i] * keep_list[i]
        string = new_string


if __name__ == '__main__':
    S = input()
    solve(S)
