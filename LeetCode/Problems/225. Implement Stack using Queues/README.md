[225. 用队列实现栈](https://leetcode-cn.com/problems/implement-stack-using-queues/)

## Ideas

队列和栈的相互操作，需要特别理解栈和队列这两种数据结构的相同点和不同点。

栈：先进后出，队列：先进先出。

既然数据结构已经限定元素进出的顺序，那么单纯的用一个队列肯定是没办法实现栈的操作的，所以我们想能不能用两个队列实现栈的操作。

首先考虑pop()操作，要移除并返回栈顶元素，假设我们有一个正常入队的队列q1，因为栈是先进后出的操作，所以我们要移除并返回的是q1的最后一个元素。

所以我们可以先把q1中的元素都出队，然后到q2入队，直到q1只剩下1个元素为止，把这个元素弹出并返回。

然后再把q2中的元素出队，入到q1中，这个操作就完成了，保证所有的元素都在q1中，这样好判断empty()和top()，

分析完了之后，我们发现push()操作只需要把元素正常入队q1就欧克了。

## Code

### Python

然后，我就发现Python的deque不仅支持append()还支持appendleft()，不仅支持pop()还支持popleft()，我擦，你这么全能干嘛，瞬间不想写了。

```python
from collections import deque


class MyStack:

	def __init__(self):
		self.q1, self.q2 = deque(), deque()

	def push(self, x: int) -> None:
		self.q1.append(x)

	def pop(self) -> int:
		return self.q1.pop()

	def top(self) -> int:
		return self.q1[-1]

	def empty(self) -> bool:
		return len(self.q1) == 0
```