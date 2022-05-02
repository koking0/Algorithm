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
