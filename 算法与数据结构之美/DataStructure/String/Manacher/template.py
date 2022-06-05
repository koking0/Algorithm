import sys


def manacher(s: str) -> int:
    s = '#' + '#'.join(list(s)) + '#'
    p_array = [0] * len(s)
    C, R, ans = -1, -1, -sys.maxsize
    for i in range(len(s)):
        p_array[i] = min(p_array[2 * C - i], R - i) if R > i else 1
        while i + p_array[i] < len(s) and i - p_array[i] > -1:
            if s[i + p_array[i]] == s[i - p_array[i]]:
                p_array[i] += 1
            else:
                break
        if i + p_array[i] > R:
            R, C = i + p_array[i], i
        ans = max(ans, p_array[i])
    return ans - 1


if __name__ == '__main__':
    str1 = "abc1234321ab"
    print(manacher(s=str1))
