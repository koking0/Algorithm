def is_square(num) -> bool:
    return int(int(num ** 0.5) ** 2) == num


def check(arr):
    tmp = []
    for idx, val in enumerate(arr):
        if val:
            tmp.append(ans[idx])

    for i in range(len(tmp)):
        for j in range(i + 1, len(tmp)):
            if is_square(tmp[i] + tmp[j]):
                return False
    print(f"len = {len(tmp)}, \t tmp = {tmp}")
    return True


def dfs(idx):
    if idx == len(ans):
        global max_ans
        if select.count(True) > max_ans and check(select):
            max_ans = max(max_ans, select.count(True))
        return
    
    select[idx] = False
    dfs(idx + 1)
    select[idx] = True
    dfs(idx + 1)


if __name__ == '__main__':
    ans = [i for i in range(1, 101) if not is_square(i)]
    
    max_ans = 0
    select = [False] * len(ans)
    dfs(0)
