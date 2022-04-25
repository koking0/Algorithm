#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/5/17 22:24
# @File     : 210. Course Schedule II.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import collections
from typing import List


class Solution:
    def findOrder_DFS(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 存储有向图
        edges = collections.defaultdict(list)
        # 标记每个节点的状态：0=》未搜索，1=》搜索中，B=》已搜索
        visited = [0] * numCourses
        # 用列表来模拟栈，索引0为栈底，n-1为栈顶
        result = list()
        # 有向图是否有环标志
        invalid = False

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal invalid
            # 将节点标记为搜索中
            visited[u] = 1
            # 搜索相邻节点
            for v in edges[u]:
                # 如果未搜索，那么搜索相邻节点
                if visited[v] == 0:
                    dfs(v)
                    # 只要发现有环，立刻停止搜索
                    if invalid:
                        return
                # 如果搜索中，说明找到了环
                elif visited[v] == 1:
                    invalid = True
                    return
            # 将节点标记为已搜索
            visited[u] = 2
            result.append(u)

        # 每次挑选一个未搜索的节点，开始进行深度优先搜索
        for i in range(numCourses):
            if not invalid and not visited[i]:
                dfs(i)

        if invalid:
            return list()

        return result[::-1]

    def findOrder_BFS(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 存储有向图
        edges = collections.defaultdict(list)
        # 存储每个节点的入度
        indeg = [0] * numCourses
        # 存储答案
        result = list()

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1

        # 将所有入度为 0 的节点放入队列中
        queue = collections.deque([u for u in range(numCourses) if indeg[u] == 0])

        while queue:
            # 从队首取出一个节点
            u = queue.popleft()
            result.append(u)
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    queue.append(v)

        if len(result) != numCourses:
            result = list()

        return result
