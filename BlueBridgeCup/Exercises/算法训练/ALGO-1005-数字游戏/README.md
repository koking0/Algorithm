[题目链接](http://lx.lanqiao.cn/problem.page?gpid=T2995)

---

## Ideas

首先想到的最暴力的方法就是全排列，枚举所有可能的排列情况，然后判断是否符合要求。

关于最后的累加和，经过分析其实可以发现结果等于各个元素乘以某个系数再相加的结果，而系数就是组合数`comb(n - 1, i) * item[i]`。

不过这样只能过90%的测试样例，所以还需要进行剪枝。

1. 可以发现，系数是可以提前计算出来的，并不需要每次check的时候再计算一遍，所以可以输入n之后直接就计算出来系数；
2. check的时候如果判断当前累加和已经大于sum了，那么后面就没必要继续计算了。

## Code

### Python

```python
from math import comb
from itertools import permutations


def check(item):
	res = 0
	for i in range(n):
		res += xi_shu[i] * item[i]
		if res > ans:
			return False
	return res == ans


def solve():
	for item in permutations(range(1, n + 1)):
		if check(item):
			print(' '.join(map(str, item)))
			return


if __name__ == '__main__':
	n, ans = map(int, input().split())
	xi_shu = [comb(n - 1, i) for i in range(n)]
	solve()
```