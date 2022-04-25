描述：正则问题

考虑一种简单的正则表达式：
只由 x ( ) | 组成的正则表达式。
小明想求出这个正则表达式能接受的最长字符串的长度。  

例如 ((xx|xxx)x|(x|xx))xx 能接受的最长字符串是： xxxxxx，长度是6。

输入

一个由x()|组成的正则表达式。输入长度不超过100，保证合法。  

输出

这个正则表达式能接受的最长字符串的长度。  

例如，
输入：
((xx|xxx)x|(x|xx))xx

程序应该输出：
6  

资源约定：
峰值内存消耗（含虚拟机） < 256M
CPU消耗  < 1000ms


请严格按要求输出，不要画蛇添足地打印类似：“请您输入...” 的多余内容。

注意：
main函数需要返回0;
只使用ANSI C/ANSI C++ 标准;
不要调用依赖于编译环境或操作系统的特殊函数。
所有依赖的函数必须明确地在源文件中 #include <xxx>
不能通过工程设置而省略常用头文件。

提交程序时，注意选择所期望的语言类型和编译器类型。

## Ideas

遇到括号匹配类似的问题，首先想到的就是用栈。

如果用栈的话有两种：① 递归用系统栈；② 自定义栈用迭代。

这里我们通过递归来实现。

这道题是想让我们求最长的x字符串长度，所以其实我们可以直接递归求长度，不再用字符串做计算了。

首先我们需要遍历整个字符串，由于是递归遍历，所有我们需要定义一个全局变量`pos`表示当前遍历到的位置索引。

然后我们先来考虑遇到`|`符号：`|`肯定连接了两个`x`字符串，我们要求其中最大的那个，所以需要定义两个变量：`tmp`和`res`，分别表示`|`左边的`x`串和右边的`x`串长度。

初始化`tmp`和`res`都是0，然后遇到`x`时让 pos + 1, tmp + 1。

此时如果遇到`|`，此时我们让`res = max(res, tmp)`，然后置 tmp 为0，代表tmp要计算`|`后面的长度。

如果遇到`)`，同样也让`res = max(res, tmp)`，然后返回 res。

如果遇到`(`，那么应该先累加pos，然后开启一个新的递归。

## Code

### C++
```cpp
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;
char s[100];
int len,pos;

int f() {
	int m = 0, tmp = 0;
	while(pos<len) {
		switch(s[pos]) {
			case '(': {
					pos++;
					tmp += f();
					break;
				}
			case ')': {
					pos++;
					m = max(m, tmp);
					return m;
				}
			case 'x': {
					pos++;
					tmp++;
					break;
				}
			case '|': {
					pos++;
					m = max(m, tmp);
					tmp = 0;
					break;
				}
		}
	}
	m = max(m, tmp);
	return m;
}

int main() {
	cin >> s;
	len = strlen(s);
	int ans = f();
	cout << ans << endl;
	return 0;
}
```

### Python
```python
def dfs():
    global pos
    res, tmp = 0, 0
    while pos < len(s):
        if s[pos] == '(':
            pos += 1
            tmp += dfs()
        elif s[pos] == ')':
            pos += 1
            res = max(res, tmp)
            return res
        elif s[pos] == 'x':
            pos += 1
            tmp += 1
        elif s[pos] == '|':
            pos += 1
            res = max(res, tmp)
            tmp = 0
    res = max(res, tmp)
    return res


if __name__ == '__main__':
    pos = 0
    s = input().strip()
    print(dfs())
```

## 在线评测：[https://www.acwing.com/problem/content/1227/](https://www.acwing.com/problem/content/1227/)