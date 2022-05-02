## Ideas

这题基本就是纯统计的活，没什么算法。

注意用四舍五入函数`round`就可以了。

同时C++注意要做类型转换。

## Code

### C++

```cpp
#include <cmath>
#include <iostream> 

using namespace std;

int main() {
	int n, n1 = 0, n2 = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int tmp;
		cin >> tmp;
		if (tmp > 59) {
			n1++;
		}
		if (tmp > 84) {
			n2++;
		}
	}
	cout << round(100.0 * n1 / n) << "%" << endl;
	cout << round(100.0 * n2 / n) << "%" << endl;
	return 0;
}
```

### Python
```python
n = int(input())
n1, n2 = 0, 0
for i in range(n):
    score = int(input())
    if score >= 85:
        n1 += 1
    if score >= 60:
        n2 += 1
print(f"{round(100 * n2 / n)}%")
print(f"{round(100 * n1 / n)}%")

```

---

在线评测：[https://www.acwing.com/problem/content/2874/](https://www.acwing.com/problem/content/2874/)