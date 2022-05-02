[1114. 按序打印](https://leetcode-cn.com/problems/print-in-order/)

## Ideas

并发执行问题是多线程要解决的经典问题，此题是典型的执行屏障问题，因此我们需要构造几把锁来确保执行顺序。

题目要求按顺序依次执行三个方法，为了保证线程的执行顺序，可以在方法之间创建一些锁，即第二个方法必须在第一个方法之后执行，第三个方法必须在第二个方法之后执行。

有两个依赖关系，所以我们定义两把锁，firstJobDone 和 secondJobDone，分别表示 first() 任务是否执行完毕和 second() 任务是否执行完毕。

我们来分析一下：
1. 首先 first() 任务没有依赖关系，也就是说它可以直接执行，执行完之后更新 firstJobDone 变量；
2. 然后 second() 任务需要 first() 任务执行完之后才能执行，也就是说 second() 任务执行之前需要检查 firstJobDone 变量，执行完之后更新 secondJobDone 变量；
3. 同理，third() 任务需要 second() 任务执行完之后才能执行，也就是说 third() 任务执行之前需要检查 secondJobDone 变量；

## Code

### Python

```python
from threading import Lock


class Foo:
	def __init__(self):
		self.firstJobDone = Lock()
		self.secondJobDone = Lock()
		self.firstJobDone.acquire()  # 一开始两个任务都没有执行过，先都锁上
		self.secondJobDone.acquire()

	def first(self, printFirst: 'Callable[[], None]') -> None:
		printFirst()
		self.firstJobDone.release()  # first() 任务执行完，解锁

	def second(self, printSecond: 'Callable[[], None]') -> None:
		with self.firstJobDone:
			printSecond()
			self.secondJobDone.release()

	def third(self, printThird: 'Callable[[], None]') -> None:
		with self.secondJobDone:
			printThird()
```