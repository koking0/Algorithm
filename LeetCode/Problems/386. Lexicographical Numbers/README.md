[386. 字典序排数](https://leetcode-cn.com/problems/lexicographical-numbers/)

## Ideas

字典序排序嘛，先生成一个数字数组，然后转成字符串类型，再排一下序，之后再转回整数数组，return就可以了。

## Code

### Python
```python
from typing import List


class Solution:
	def lexicalOrder(self, n: int) -> List[int]:
		num_list = list(range(1, n + 1))
		str_list = list(map(str, num_list))
		str_list.sort()
		return list(map(int, str_list))


if __name__ == '__main__':
	print(Solution().lexicalOrder(13))
```