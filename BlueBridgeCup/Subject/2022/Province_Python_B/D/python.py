if __name__ == '__main__':
    n = int(input())
    m = int(input())
    
    num_list = [str(i) for i in range(1, n + 1)]
    num_list.sort(key=lambda x: sum(map(int, list(x))))
    print(num_list[m - 1])
