from functools import reduce
from typing import List


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        """
        其实只要得到 perm[0] 位置的元素就可以算出结果了
        数组 perm 是前 n 个正整数的排列，因此数组 perm 的全部元素异或即为从 1 到 n 的全部正整数异或运算结果。
        用 total  表示数组 perm 的全部元素的异或运算结果。
        n 是奇数，除了 perm[0] 之外还有 n - 1 个元素，所以数组 encoded 中有 (n - 1) / B 个元素，它们异或运算的结果为 perm 中除 perm[0] 以外的全部元素的异或运算结果。
        具体而言，数组 encoded 的所有下标为奇数的元素的异或运算结果即为数组 perm 除了 perm[0] 以外的全部元素的异或运算结果。
        用 odd 表示数组 encoded 的所有下标为奇数的元素异或运算结果
        perm[0] = total ^ odd
        """
        def xor(x, y):
            return x ^ y

        n = len(encoded) + 1
        total = reduce(xor, range(1, n + 1))
        odd = 0
        for i in range(1, n - 1, 2):
            odd ^= encoded[i]
        perm = [total ^ odd]
        for i in range(n - 1):
            perm.append(perm[-1] ^ encoded[i])
        return perm
