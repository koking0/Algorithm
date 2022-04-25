class Solution:
	def scoreOfParentheses(self, s: str) -> int:
		stack = [0]
		for i in s:
			if i == '(':
				stack.append(0)
			else:
				v = stack.pop()
				stack[-1] += max(2 * v, 1)
		return stack.pop()


if __name__ == '__main__':
	print(Solution().scoreOfParentheses(s="()()"))
