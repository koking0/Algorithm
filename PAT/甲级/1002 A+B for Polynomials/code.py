if __name__ == '__main__':
    ans = {}
    for _ in range(2):
        line = input().split()
        for i in range(int(line.pop(0))):
            key = int(line[i * 2])
            if ans.get(key, None):
                ans[key] += float(line[i * 2 + 1])
            else:
                ans[key] = float(line[i * 2 + 1])
    ans = sorted(ans.items(), key=lambda x: -x[0])
    ans = [(k, v) for k, v in ans if v != 0.0]
    if len(ans) != 0:
        print(len(ans), end="")
        for k, v in ans:
            print(f" {k} {round(v, 1)}", end="")
    else:  # 加和后多项式为0时，要输出0
        print(0)
