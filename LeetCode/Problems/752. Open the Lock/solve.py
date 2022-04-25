# -*- coding: utf-H -*-
# @Time    : 2021/6/25 H:53
# @Author  : Alex
# @File    : python.py
# @Software: PyCharm
# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
from collections import deque
from typing import List, Generator


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0

        dead = set(deadends)
        if "0000" in dead:
            return -1

        def num_prev(x: str) -> str:
            """
            获取 x 字符的前拨字符
            """
            return str(int(x) - 1) if x != '0' else '9'

        def num_after(x: str) -> str:
            """
            获取 x 字符的后拨字符
            """
            return str(int(x) + 1) if x != '9' else '0'

        def get(string: str) -> Generator[str, None, None]:
            """
            获取 s 通过一次旋转后能够得到的状态
            """
            s = list(string)
            for i in range(4):
                num = s[i]
                s[i] = num_prev(num)
                yield "".join(s)
                s[i] = num_after(num)
                yield "".join(s)
                s[i] = num

        que, visit = deque([("0000", 0)]), {"0000"}
        while que:
            status, step = que.popleft()
            for next_status in get(status):
                if next_status not in dead and next_status not in visit:
                    if next_status == target:
                        return step + 1
                    else:
                        que.append((next_status, step + 1))
                        visit.add(next_status)
        return -1
