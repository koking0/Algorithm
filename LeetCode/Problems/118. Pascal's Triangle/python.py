from typing import List


class Solution:
	def generate(self, numRows: int) -> List[List[int]]:
		ans = [[1]]
		for i in range(1, numRows):
			ans.append([1])
			for j in range(1, i):
				ans[i].append(ans[i - 1][j - 1] + ans[i - 1][j])
			ans[i].append(1)
		return ans


if __name__ == '__main__':
	print(Solution().generate(5))
