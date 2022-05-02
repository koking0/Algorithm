from typing import List


class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		total = [[""]]
		for i in range(1, n + 1):
			cur = list()  # 用于存储增加一对括号后可能生成的所有情况
			for j in range(i):
				item_p = total[j]
				item_q = total[i - 1 - j]
				for p in item_p:
					for q in item_q:
						cur.append(f"({p}){q}")
			total.append(list(cur))
		return total[n]


if __name__ == '__main__':
	print(Solution().generateParenthesis(4))
