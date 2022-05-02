## Ideas

首先我们根据数学常识可以知道，当每个机器人清扫的范围差不多时，最好都是 N / K，花的时间应该是最少的。

所以这道题实际上就是让我们搜索每个机器人负责清扫的范围，我们假设这个范围是x。

既然是搜索，那么首先想到的就是二分，不断的缩小x的过程中确保所有机器人的清扫范围能够覆盖N个方格。

二分不是很麻烦，所以重点是确保所有机器人的清扫范围能够覆盖N个方格。

给定一个x之后，我们可以遍历每个机器人所在的位置依次判断，因为题目中给出的机器人的位置并不是有序的，所以读入数据之后还要先排序。

我们可以设置一个 total 变量，表示从左到右依次能够清扫的范围。

对于每一个机器人所在的位置k[i]，如果k[i] - x，也就是机器人能够清扫的左边界小于total的话，分成两种情况：

1. k[i] < total: 说明前面一个机器人k[i - 1]能够清扫的右边界达到k[i]的起始位置，那么第i个机器人就不用往左边走了，此时前i个机器人能够清扫的total = k[i] + x - 1；
2. k[i] >= total: 说明前面一个机器人k[i - 1]能够清扫的右边界没有达到k[i]的起始位置，那么第i个机器人就需要往左边清扫，而此时前i个机器人能够清扫的total = total + x；

如果 k[i] - x > total 的话，也就是第 i 个机器人能够清扫的左边界都大于前 i - 1 个机器人能够清扫到的范围，那说明这个 x 选的太小了，得增大范围。

最后找到了合适的 x 之后，那么花费时间最长的机器人，就是这个机器人的位置正好在 x 的中间，它需要先往左扫，再回来，然后往右扫，再回来，所以花费的最长时间为 (x - 1) * 2。

然后我们就可以开始写代码啦。

## Code

### C++

```cpp
#include <iostream>
#include <algorithm>

using namespace std;

const int maxn = 1e5+7;
int n, m;
int robot_list[maxn];

bool check(int x) {
	int total = 0;
	for (int i = 0; i < m; i++) {
		if (robot_list[i] - x < total + 1) {
			if (robot_list[i] < total + 1) {
				total = robot_list[i] + x - 1;
			} else {
				total += x;
			}
		} else {
			return false;
		}
	}
	return total > n - 1;
}

int main() {
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		cin >> robot_list[i];
	}
	sort(robot_list, robot_list + m);	
	
	int left = 0, right = n, middle, ans;
	while (left < right + 1) {
		middle = (right + left) >> 1;
		if (check(middle)) {
			right = middle - 1;
			ans = middle;
		} else {
			left = middle + 1;
		}
	}
	cout << (ans - 1) * 2 << endl;
	return 0;
}
```

### Python

```python
def check(x):
	total = 0   # 前面的机器人能够清扫的右边界，初始化为0
	for i, v in enumerate(robot_list):
		if v - x < total + 1:
			if v < total + 1:
				total = v + x - 1
			else:
				total += x
		else:
			return False
	return total > n - 1


if __name__ == '__main__':
	# 1. 处理输入数据
	n, k = map(int, input().split())
	robot_list = []
	for _ in range(k):
		robot_list.append(int(input()))
	robot_list.sort()

	# B. 二分查找
	left, right, ans = 0, n, n
	while left < right + 1:
		middle = (right + left) >> 1
		if check(middle):   # 如果此时确定的清扫范围可以满足条件则继续缩小范围
			ans = middle
			right = middle - 1
		else:
			left = middle + 1

	print((ans - 1) * 2)
```