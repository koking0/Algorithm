[](./images/7.png)
[](./images/8.png)

## Ideas

这道题目其实主要就是数据处理，可以先把所有的成绩都存到一个数组里，最后统一处理。（Python代码）

当让也有更高级的处理，我们可以在读入数据的过程中就分别维护三个变量：最大值、最小值、所有学生总分，读入完所有数据之后再用总分除以总人数就得到了平均分。（C++代码）

## Code

### C++

```cpp
#include <climits>
#include <iomanip>
#include <iostream>

using namespace std;

int main() {
	int n, max_num = INT_MIN, min_num = INT_MAX, sum = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int num;
		cin >> num;
		max_num = max(max_num, num);
		min_num = min(min_num, num);
		sum += num;
	}
	cout << max_num << endl << min_num << endl << fixed << setprecision(2) << 1.0 * sum / n << endl;
	return 0;
}
```

### Python

```python
if __name__ == '__main__':
    nums = [int(input()) for _ in range(int(input()))]
    print(f"{max(nums)}\n{min(nums)}\n{(sum(nums) / len(nums)):.2f}")
```