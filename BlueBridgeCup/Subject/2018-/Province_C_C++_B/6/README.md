## 递增三元组

给定三个整数数组
A = [A1, A2, ... AN], 
B = [B1, B2, ... BN], 
C = [C1, C2, ... CN]，
请你统计有多少个三元组(i, j, k) 满足：
1. 1 <= i, j, k <= N  
2. Ai < Bj < Ck  

【输入格式】 
第一行包含一个整数N。
第二行包含N个整数A1, A2, ... AN。
第三行包含N个整数B1, B2, ... BN。
第四行包含N个整数C1, C2, ... CN。

对于30%的数据，1 <= N <= 100  
对于60%的数据，1 <= N <= 1000 
对于100%的数据，1 <= N <= 100000 0 <= Ai, Bi, Ci <= 100000 

【输出格式】
一个整数表示答案

【样例输入】
3
1 1 1
2 2 2
3 3 3

【样例输出】
27 


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

首先我们要根据输入数据的量级确定最终满足要求的算法时间复杂度。

如果是用三层暴力循环求递增三元组，那么算法的时间复杂度就是O(N ^ 3)，肯定不可能过所有的数据。

对于100%的数据，1 <= N <= 100000，所以最终满足要求的算法时间复杂度应该是O(n * logn)的。

然后再来看题目要求，并没有要求 i j k 的大小，所以我们可以先给三个数组进行升序排序。

然后对于B数组中的每一个数bi，我们可以在A数组中找到一个小于bi的最大数a，对应的索引为a_idx，同样可以在C数组中找到一个大于bi的最小数b,对应的索引为b_idx。

根据a_idx和b_idx，我们可以求出对应A数组中小于bi的元素个数 num_1，也可以求出C数组中大于bi的元素个数 num_2，根据乘法原理，bi对应的符合条件的递增三元组个数为 num_1 * num_2。

遍历整个B数组，对于每个元素bi都在A、B数组中求出相应的 num_1 * num_2，最后累加在一起就可以了。

## Code 

### Python

```python
from bisect import bisect_left, bisect_right

if __name__ == '__main__':
	ans = 0
	n = int(input())
	A = sorted(list(map(int, input().split())))
	B = sorted(list(map(int, input().split())))
	C = sorted(list(map(int, input().split())))
	
	for item in B:
		num_1 = bisect_left(A, item)
		num_2 = n - bisect_right(C, item)
		print(num_1, num_2)
		ans += num_1 * num_2
	print(ans)
```