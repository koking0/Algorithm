import collections
from typing import List


class Solution(object):
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n, ans = len(A), 0
        que = collections.deque()
        for i in range(n):
            if que and i > que[0] + K - 1:
                que.popleft()
            if len(que) % 2 == A[i]:
                if i + K > n:
                    return -1
                que.append(i)
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minKBitFlips(A=[0, 0, 0, 1, 0, 1, 1, 0], K=3))
