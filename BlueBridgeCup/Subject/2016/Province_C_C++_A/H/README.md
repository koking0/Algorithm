## 题目

四平方和

四平方和定理，又称为拉格朗日定理：
每个正整数都可以表示为至多4个正整数的平方和。
如果把0包括进去，就正好可以表示为4个数的平方和。

比如：
5 = 0^2^ + 0^2^ + 1^2^ + 2^2^
7 = 1^2^ + 1^2^ + 1^2^ + 2^2^
（^符号表示乘方的意思）

对于一个给定的正整数，可能存在多种平方和的表示法。
要求你对4个数排序：
0 <= a <= b <= c <= d
并对所有的可能表示法按 a,b,c,d 为联合主键升序排列，最后输出第一个表示法


程序输入为一个正整数N (N<5000000)
要求输出4个非负整数，按从小到大排序，中间用空格分开

例如，输入：
5
则程序应该输出：
0 0 1 2

再例如，输入：
12
则程序应该输出：
0 2 2 2

再例如，输入：
773535
则程序应该输出：
1 1 267 838

资源约定：
峰值内存消耗 < 256M
CPU消耗  < 3000ms

请严格按要求输出，不要画蛇添足地打印类似：“请您输入...” 的多余内容。

所有代码放在同一个源文件中，调试通过后，拷贝提交该源码。

注意: main函数需要返回0
注意: 只使用ANSI C/ANSI C++ 标准，不要调用依赖于编译环境或操作系统的特殊函数。
注意: 所有依赖的函数必须明确地在源文件中 #include <xxx>， 不能通过工程设置而省略常用头文件。

提交时，注意选择所期望的编译器类型。

## Ideas

首先，因为n = a^2^ + b^2^ + c^2^ + d^2^，所以 $a,b,c,d < \sqrt{n}$。

然后因为N<5000000，所以我们必须要保证算法的时间复杂度在O(nlogn)以内。

所以四层暴力循环肯定会超时的，对于$\sqrt{n}$的循环我们最多只能有两层。

那么我们就想怎么能把四层循环拆成两层，然后还得保证算法的时间复杂度在O(nlogn)以内。

对于$\sqrt{n}$的循环我们最多只能有两层，也就是说循环的时间复杂度就达到了O(n)，符合小于O(nlogn)的限制。

那么怎么拆成两个循环呢？

前两个循环：我们可以先枚举两个比较大的数c和d，然后把所有$c^{2} + d^{2}$的结果都存储到一个哈希表中，key就是$c^{2} + d^{2}$，value就是(c, d)。

后两个循环：枚举a和b，然后我们判断$num - (a^{2} + b^{2})$的结果是否在集合中，如果在的话，那就说明我们找到了答案。

## Code

### Python 
```python
def solve(num):
	hash_table = dict()
	for c in range(int(num ** 0.5) + 1):
		for d in range(c, int(num ** 0.5) + 1):  # d可以从c开始枚举
			val = c ** 2 + d ** 2
			if not hash_table.get(val, None):
				hash_table[val] = f"{c} {d}"
	for a in range(int(num ** 0.5) + 1):
		for b in range(a, int(num ** 0.5) + 1):
			val = hash_table.get(num - a ** 2 - b ** 2)
			if val:
				print(f"{a} {b} {val}")
				return


if __name__ == '__main__':
	solve(int(input()))
```

## 在线评测：[https://www.acwing.com/problem/content/1223/](https://www.acwing.com/problem/content/1223/)