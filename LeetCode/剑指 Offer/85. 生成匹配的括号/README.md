[22. 括号生成](https://leetcode-cn.com/problems/generate-parentheses/)

## Ideas

这是一道动态规划的题目，关于动态规划的题目我们可以从n比较小的情况下开始逐步分析。

当n=1时，["()"]

当n=2时，["()()", "(())"]

当n=3时，["()()()", "(()())", "()(())", "(())()", "((()))"]

什么意思呢？

当n=1，也就是只有一对括号时，只有一种情况。

当n=2时，其实是在只有一对括号的情况下添加一对括号，可以添加在左边，也就是"()()"，可以直接在外面套一层括号，也就是"(())"，添加到右边的情况就和添加到左边的情况一样的了。

同理，当n=3时，我们是在n=2的所有情况中添加一对括号，添加的形式有三种，左边、右边、外面套一层。

以此类推，如果我们知道了 i < n 时的所有情况，就可以对所有情况进行组合遍历：

f"({i = p 时的所有情况}){i = n - 1 -p 时的所有情况}"

可以把 i = p 时的所有情况 定义为p，i = n - 1 -p 时的所有情况 定义为 q。

然后就是遍历组合啦。

## Code 

### Python 

```python
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
```