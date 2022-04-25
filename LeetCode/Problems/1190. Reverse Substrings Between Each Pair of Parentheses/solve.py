class Solution:
    def reverseParentheses(self, s: str) -> str:
        """
        准备一个 stack，遍历 s，如果是字母或者左括号，直接 append 到 stack 中。
        如果遍历过程中遇到右括号，从 stack 中弹出字母直到左括号，然后将弹出的字母拼起来反转，再添加回 stack。
        """
        stack = list()
        for ch in s:
            if ch == ')':
                cur_list = list()
                while stack[-1] != '(':
                    tail_ch = stack.pop()
                    cur_list.append(tail_ch)
                stack.pop()
                stack.extend(cur_list)
            else:
                stack.append(ch)
        return ''.join(stack)


if __name__ == '__main__':
    print(Solution().reverseParentheses(s="a(bcdefghijkl(mno)p)q"))
