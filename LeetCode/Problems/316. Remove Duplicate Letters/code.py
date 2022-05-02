class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        for i, ch in enumerate(s):
            if ch not in stack:
                while stack and ch < stack[-1] and stack[-1] in s[i:]:
                    stack.pop()
                stack.append(ch)
        return "".join(stack)


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicateLetters("cbacdcbc"))
