if __name__ == '__main__':
    n = int(input())
    student_time_list = []
    for _ in range(n):
        student_time_list.append(list(map(int, input().split())))
    
    ans = 0
    student_time_list.sort(key=lambda x: sum(x))
    for i in range(n):
        ans += (n - i) * sum(student_time_list[i])
        ans -= student_time_list[i][-1]
    print(ans)
