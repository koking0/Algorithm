[试题 算法提高 队列操作](http://lx.lanqiao.cn/problem.page?gpid=T418)

## Ideas

这题没什么技巧吧，用数组来模拟队列操作，按照指令来就可以了，帮助回忆一下队列的一些操作。

## Code

### Python

```python
def solve():
	queue = list()
	n = int(input())
	for _ in range(n):
		string = input()
		if string[0] == '1':  # 入队操作
			queue.append(string.split(' ')[1])
		elif string[0] == '2':  # 出队操作
			if queue:
				print(queue.pop(0))
			else:
				print("no")
				return
		elif string[0] == '3':  # 计算队中元素个数并输出
			print(len(queue))


if __name__ == '__main__':
	solve()
```