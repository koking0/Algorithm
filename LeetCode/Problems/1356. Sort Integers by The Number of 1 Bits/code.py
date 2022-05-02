import collections

from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        d = dict()
        for i in arr:
            if d.get(bin(i).count('1'), None):
                d[bin(i).count('1')].append(i)
            else:
                d[bin(i).count('1')] = [i]
        d = collections.OrderedDict(sorted(d.items(), key=lambda t: t[0]))
        a = []
        for _, v in d.items():
            for item in v:
                a.append(item)
        return a


if __name__ == '__main__':
    s = Solution()
    ans = s.sortByBits(arr=[10, 100, 1000, 10000])
    print(ans)
