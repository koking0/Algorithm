import string


"""19本来就是奇数个，每次删除奇数位之后还是奇数个，所以只在19位之内模拟也是可以的。"""
s = string.ascii_lowercase[:19] * 106
print(s)
while len(s) > 1:
    for i in range(len(s)):
        if i & 1:
            s = s[:i] + s[i + 1:]
print(s)
