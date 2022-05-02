[274. H 指数](https://leetcode-cn.com/problems/h-index/)

## Ideas

H指数表示的是有h篇论文被引用了至少h次。

我们可以将citations逆序排列，表示引用次数从高到底排列。

如果我们从前向后遍历数组，那么第i位上值v，就表示至少有i篇文章引用次数大于等于v。

此时如果i又大于等于v，那么就说明第i位至少有i篇文章。

又因为i是下标，所以要判断 i + 1 和 v 的值。

## Code

### Python

```python
class Solution:
	def hIndex(self, citations: List[int]) -> int:
		citations.sort(reverse=True)
		for i, v in enumerate(citations):
			if i + 1 > v:
				return i
		return len(citations)
```