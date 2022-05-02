class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n != 1 and n not in visit:
            visit.add(n)
            new = list(map(int, list(str(n))))
            for i, v in enumerate(new):
                new[i] = v ** 2
            n = sum(new)
        return n == 1


if __name__ == '__main__':
    print(Solution().isHappy(19))
