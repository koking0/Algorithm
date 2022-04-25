from collections import Counter
from typing import List


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def subsets(ws: List[int]) -> List[List[int]]:
            res = [""]
            for i in ws:
                res += [i + w for w in res]
            print(res)
            return res

        cnt = Counter()
        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            cnt[mask] += 1
        res = []
        for puzzle in puzzles:
            total = 0
            for perm in subsets(puzzle[1:]):
                mask = 1 << (ord(puzzle[0]) - ord('a'))
                for c in perm:
                    mask |= 1 << (ord(c) - ord('a'))
                total += cnt[mask]
            res.append(total)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findNumOfValidWords(words=["aaaa", "asas", "able", "ability", "actt", "actor", "access"],
                                puzzles=["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]))
