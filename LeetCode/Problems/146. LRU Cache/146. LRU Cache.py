#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/5/25 22:09
# @File     : 146. LRU Cache.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import collections


class LRUCache_1(collections.OrderedDict):

	def __init__(self, capacity: int):
		super().__init__()
		self.capacity = capacity

	def get(self, key: int) -> int:
		if key not in self:
			return -1
		self.move_to_end(key=key)
		return self[key]

	def put(self, key: int, value: int) -> None:
		if key in self:
			self.move_to_end(key=key)
		self[key] = value
		if len(self) > self.capacity:
			self.popitem(last=False)


class DoubleLinkNode:
	def __init__(self, key=0, value=0):
		self.key, self.value, self.prev, self.next = key, value, None, None


class LRUCache:

	def __init__(self, capacity: int):
		self.cache, self.capacity, self.size = dict(), capacity, 0
		self.head, self.tail = DoubleLinkNode(), DoubleLinkNode()
		self.head.next, self.tail.prev = self.tail, self.head

	def get(self, key: int) -> int:
		if key not in self.cache:
			return -1
		# 如果 key 存在，先通过哈希表定位，再移到头部
		node = self.cache[key]
		self.moveToHead(node)
		return node.value

	def put(self, key: int, value: int) -> None:
		if key not in self.cache:
			# 如果 key 不存在，创建一个新的节点
			node = DoubleLinkNode(key, value)
			# 添加进哈希表
			self.cache[key] = node
			# 添加至双向链表的头部
			self.addToHead(node)
			self.size += 1
			if self.size > self.capacity:
				# 如果超出容量，删除双向链表的尾部节点
				removed = self.removeTail()
				# 删除哈希表中对应的项
				self.cache.pop(removed.key)
				self.size -= 1
		else:
			# 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
			node = self.cache[key]
			node.value = value
			self.moveToHead(node)

	def addToHead(self, node):
		node.prev = self.head
		node.next = self.head.next
		self.head.next.prev = node
		self.head.next = node

	def removeNode(self, node):
		node.prev.next = node.next
		node.next.prev = node.prev

	def moveToHead(self, node):
		self.removeNode(node)
		self.addToHead(node)

	def removeTail(self):
		node = self.tail.prev
		self.removeNode(node)
		return node
