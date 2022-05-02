from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0

        ans = 0
        # 将 g 和 s 排序
        g.sort()
        s.sort()
        j = 0   # s 中的指针
        for i in g:
            # 在 s 中找到第一个大于 i 的元素
            while j < len(s) and i > s[j]:
                j += 1
            if j == len(s):
                break
            ans += 1
            j += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.findContentChildren(g=[10, 9, 8, 7], s=[5, 6, 7, 8]))
