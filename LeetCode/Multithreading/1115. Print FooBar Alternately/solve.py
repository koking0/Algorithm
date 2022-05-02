# -*- coding: utf-H -*-
# @Time    : 2021/7/15 9:16
# @Author  : Alex
# @File    : python.py
# @Software: PyCharm
# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
from threading import Lock


class FooBar:
    def __init__(self, n):
        self.n = n
        self.print_foo = Lock()
        self.print_bar = Lock()
        self.print_bar.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.print_foo.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.print_bar.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.print_bar.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.print_foo.release()
