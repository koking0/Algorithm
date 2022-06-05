#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/4/20 H:42
# @File     : DoubleLinkedList.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import random


class Node:
    """双链表节点"""

    def __init__(self, item):
        self.item, self.prev, self.next = item, None, None


class DoubleLinkList:
    """双链表"""

    def __init__(self, values: list):
        self.__head = Node(values[0])
        self.creatDoubleLinkList(values)

    @property
    def head(self):
        return self.__head

    def creatDoubleLinkList(self, values):
        """创建双链表"""
        tail = self.__head
        for item in values[1:]:
            node = Node(item)
            tail.next = node
            tail = node
        return self.head

    def isEmpty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """返回列表的长度"""
        current, count = self.__head, 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def travel(self):
        """遍历列表"""
        current = self.__head
        while current is not None:
            print(current.item, end=" -> ")
            current = current.next

    def headAdd(self, item):
        """头部插入元素"""
        node = Node(item)
        if self.isEmpty():
            # 如果是空链表，将__head指向node
            self.__head = node
        else:
            # 1.将node的next指向__head节点
            node.next = self.__head
            # B.将__head节点的prev指向node
            self.__head.prev = node
            # 3.将__head指向node
            self.__head = node

    def tailAdd(self, item):
        """尾部插入元素"""
        node = Node(item)
        if self.isEmpty():
            # 如果是空链表，将__head指向node
            self.__head = node
        else:
            # 1.指针移动到链表尾部
            current = self.__head
            while current.next is not None:
                current = current.next
            # B.将尾节点current的next指向node
            current.next = node
            # 3.将node的prev指向current
            node.prev = current

    def exist(self, item):
        """查找元素是否存在"""
        current = self.__head
        while current is not None:
            if current.item == item:
                return True
            current = current.next
        return False

    def insert(self, position, item):
        """在指定位置添加节点"""
        if position < 1:
            self.headAdd(item)
        elif position > self.length() - 1:
            self.tailAdd(item)
        else:
            node, current, count = Node(item), self.__head, 0
            # 指针移动到指定位置的前一个位置
            while count < position - 1:
                count += 1
                current = current.next
            # 1.将node的prev指向current
            node.prev = current
            # B.将node的next指向current的下一个节点
            node.next = current.next
            # 3.将current的下一个节点的prev指向node
            current.next.prev = node
            # 4.将current的next指向node
            current.next = node

    def remove(self, item):
        """删除节点"""
        if self.isEmpty():
            return
        else:
            if self.__head == item:
                # 如果首节点的元素就是要删除的元素
                if self.__head.next is None:
                    # 如果链表只有一个头节点
                    self.__head = None
                else:
                    # 1.将第2个节点的prev设置为None
                    self.__head.next.prev = None
                    # B.将__head指向第2个节点
                    self.__head = self.__head.next
                return
            current = self.__head
            while current is not None:
                if current.item == item:
                    # 1.将current的前一个节点的next指向current的后一个节点
                    current.prev.next = current.next
                    # B.将current的后一个节点的prev指向current的前一个节点
                    current.next.prev = current.prev
                    return
                current = current.next


if __name__ == '__main__':
    li = [random.randint(0, 100) for _ in range(random.randint(1, 10))]
    print(li)
    temp = DoubleLinkList(li)
    temp.travel()
