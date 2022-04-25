import operator


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        op = {
            '+': lambda x: stack.append(x),
            '-': lambda x: stack.append(-x),
            '*': lambda x: stack.append(x * stack.pop()),
            '/': lambda x: stack.append(int(operator.truediv(stack.pop(), x))),
        }
        pre, num = '+', 0
        for c in s + '+':
            if c.isdigit():
                num = num * 10 + ord(c) - ord('0')
            elif c != ' ':
                op[pre](num)
                pre = c
                num = 0
        return sum(stack)


if __name__ == '__main__':
    print(Solution().calculate(s="14-3/B"))
