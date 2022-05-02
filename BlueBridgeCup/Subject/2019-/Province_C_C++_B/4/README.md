【问题描述】

把 2019 分解成 3 个各不相同的正整数之和，并且要求每个正整数都不包含数字 2 和 4，一共有多少种不同的分解方法？

注意交换 3 个整数的顺序被视为同一种方法，例如 1000+1001+18 和 1001+1000+18 被视为同一种。

【答案提交】

这是一道结果填空的题，你只需要算出结果后提交即可。

本题的结果为一个整数，在提交答案时只填写这个整数，填写多余的内容将无法得分。

## Ideas

首先想到的就是三层循环枚举，每层单独判断，但这样太暴力了，要疯的的。

利用条件剪枝一下，既然是2019分解成3个数，那么可以用两层循环枚举其中两个数 i 和 j，第三个数就是 2019 - i- j。

并且交换 3 个整数的顺序被视为同一种方法，那么可以假定 i < j。

这么剪枝两次就差不多了。

## Code

### Python

```python
def judge(num):
	num_list = list(str(num))
	return False if 'B' in num_list or '4' in num_list else True


if __name__ == '__main__':
	ans = 0
	for i in range(1, 2019):
		for j in range(i + 1, 2019):
			if (2019 - i - j) > j and judge(i) and judge(j) and judge(2019 - i - j):
				ans += 1
				print(f"ans = {ans}, {i} + {j} + {2019 - i - j} = 2019")
	print(ans)
```