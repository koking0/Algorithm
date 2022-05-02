from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for item in A:
            item.reverse()
            for i in range(len(item)):
                item[i] ^= 1
        return A


if __name__ == '__main__':
    s = Solution()
    print(s.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
