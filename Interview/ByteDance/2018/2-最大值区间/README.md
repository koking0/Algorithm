## 字节跳动2018校招算法方向（第一批） —— 最大值区间

时间限制：C/C++ 3秒，其他语言6秒

空间限制：C/C++ 128M，其他语言256M

给定一个数组序列, 需要求选出一个区间, 使得该区间是所有区间中经过如下计算的值最大的一个：

区间中的最小数 * 区间所有数的和最后程序输出经过计算后的最大值即可，不需要输出具体的区间。如给定序列  [6 2 1]则根据上述公式, 可得到所有可以选定各个区间的计算值:

[6] = 6 * 6 = 36;

[2] = 2 * 2 = 4;

[1] = 1 * 1 = 1;

[6,2] = 2 * 8 = 16;

[2,1] = 1 * 3 = 3;

[6, 2, 1] = 1 * 9 = 9;
 

从上述计算可见选定区间 [6] ，计算值为 36， 则程序输出为 36。

区间内的所有数字都在[0, 100]的范围内;

### 输入描述:

第一行输入数组序列长度n，第二行输入数组序列。

对于 50%的数据,  1 <= n <= 10000;

对于 100%的数据, 1 <= n <= 500000;

### 输出描述:

输出数组经过计算后的最大值。

### 输入例子1:

```
3
6 2 1
```

### 输出例子1:

```
36
```

## Ideas

最简单的暴力法直接两层循环，但是不用想，肯定超时。

区间问题一般有两种解法，一种是滑动窗口，用双指针不断尝试，一种是区间伸缩，尝试以数组中每一个数为中心，在满足要求的前提下向外扩展。

详细来说，对于数组的每一个数，以它为区间最小值都对应一个最大值区间，那么以第i个数为中心，分别向左右两边伸展，直到遇到比该数更小的数为止，即可伸展得到一个区间。

在伸展的过程中同时可以累加遍历到的数，这样伸展结束后可以直接将该数与累加和相乘，得到区间最大值。

## Code

### Python

1. 暴力法

```python
if __name__ == '__main__':
	n = int(input())
	nums = list(map(int, input().split()))
	
	ans = 0
	for i in range(n):
		for j in range(i + 1, n):
			min_num = min(nums[i:j])
			total = sum(nums[i:j])
			ans = max(ans, min_num * total)
	print(ans)
```

2. 区间伸展法

```python
def solve2():
	res = 0
	for i in range(n):
		if nums[i] != 0:
			sum_tmp = nums[i]
			left = right = i
			while left - 1 > -1 and nums[left - 1] >= nums[i]:
				sum_tmp += nums[left - 1]
				left -= 1
			while right + 1 < n and nums[right + 1] >= nums[i]:
				sum_tmp += nums[right + 1]
				right += 1
			res = max(res, nums[i] * sum_tmp)
	return res


if __name__ == '__main__':
	n = int(input())
	nums = list(map(int, input().split()))
	
	print(solve2())
```