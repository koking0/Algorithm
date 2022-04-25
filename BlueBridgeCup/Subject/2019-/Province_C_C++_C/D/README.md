## Ideas

本来一开始想到的是质数筛，但是埃式筛是用来筛选 n 以内的所有质数，并不能找到第 n 个质数，除非找到一个足够大的 n 能够把第 2019 个质数包含进去。

可能质数筛还有升级，能够用来找到第 n 个质数，挖个坑，后面研究一下。

所以这题就用来最原始的方法：通过一个函数 `is_primer()` 来判断一个数是不是质数，逻辑就是从2开始检查，一直到根号n为止，如果发现n的约数，那么就说明n不是质数。

## Code

### Python

```python
def is_primer(n):
	for i in range(2, int((n ** 0.5) + 1)):
		if n % i == 0:
			return False
	return True


if __name__ == '__main__':
	num = 2
	primer_num = list()
	while len(primer_num) < 2019:
		if is_primer(num):
			primer_num.append(num)
		num += 1
	print(primer_num[-1])
```