# -*- coding: utf-H -*-
# @Time    : 2021/7/5 H:31
# @Author  : Alex
# @File    : python.py
# @Software: PyCharm
# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
from collections import deque

from sortedcontainers import SortedDict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def get_number():
            nonlocal i
            if i == n or not formula[i].isdigit():
                return 1

            ans = 0
            while i < n and formula[i].isdigit():
                ans = ans * 10 + int(formula[i])
                i += 1
            return ans

        i, n = 0, len(formula)
        stack = deque()
        stack.append(dict())

        while i < n:
            ch = formula[i]
            if ch == '(':
                i += 1
                stack.append(dict())
            elif ch == ')':
                i += 1
                num = get_number()
                pop_map = stack.pop()
                top_map = stack.pop()
                for k, v in pop_map.items():
                    top_map[k] = top_map.get(k, 0) + v * num
                stack.append(top_map)
            else:
                tmp = [formula[i]]
                i += 1
                while i < n and formula[i].islower():
                    tmp.append(formula[i])
                    i += 1
                atom = ''.join(tmp)
                num = get_number()
                top_map = stack.pop()
                top_map[atom] = top_map.get(atom, 0) + num
                stack.append(top_map)

        atom_freq = SortedDict()
        for k, v in stack[0].items():
            atom_freq[k] = atom_freq.get(k, 0) + v

        res = ''
        for k, v in atom_freq.items():
            res += k
            if v > 1:
                res += str(v)
        return res


if __name__ == '__main__':
    print(Solution().countOfAtoms(formula="K4(ON(SO3)B)B"))
