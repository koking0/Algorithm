## Ideas

emmmm，按照杨辉三角的定义生成就好咯。

首先杨辉三角是一个二维结构，所以肯定需要通过两层循环来生成。

对于外层循环很简单的，我们要生成numRows行，那么直接循环numRows次就可以了。

对于内层循环，可以发现，杨辉三角的第n行有n个元素，而且头尾都是1，所以也很简单。

对于第1行来说，我们可以直接在创建数组的时候预定义好，那么后面就可以直接按照统一的逻辑来，不用单独处理了。

## Code 

### Python

```python
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
```