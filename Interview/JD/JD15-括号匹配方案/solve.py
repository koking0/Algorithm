if __name__ == '__main__':
    ans = 1
    stack = []
    s = input()
    for i in s:
        if i == '(':
            stack.append('(')
        else:
            ans *= len(stack)
            stack.pop()
    print(ans)
