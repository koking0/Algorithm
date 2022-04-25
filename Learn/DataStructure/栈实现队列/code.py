#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/1/19 下午9:42
# @File     : BubbleSortCode.py
# @Project  : Algorithm
# @Software : PyCharm
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
# 一开始还想找一下python内置的栈模块，然后突然间发现，列表不就是一个栈结构么


class MyQueue(object):

    def __init__(self):
        """
        Initialize data structure
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, value):
        """
        Push element value to the back of queue
        push进入模拟队列的元素直接放进stack1里
        :param value: int
        :return: void
        """
        self.stack1.append(value)

    def pop(self):
        """
        Removes the element from in front od queue and returns that element
        pop弹出模拟队列队首的元素时，如果stack2不为空，
        将stack1中的元素全部倒进stack2中，然后返回stack2的最后一个元素，
        最后再将stack2中的元素倒回stack1中
        :return: int
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        res = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return res

    def peek(self):
        """
        Get the front element
        :return: int
        """
        return self.stack1[0]

    def empty(self):
        """
        Return whether the queue is empty
        :return: bool
        """
        return not self.stack1