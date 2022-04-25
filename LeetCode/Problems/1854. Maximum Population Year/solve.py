from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        cnt = [0 for _ in range(1950, 2051)]
        for birth, death in logs:
            for i in range(birth, death):
                cnt[i - 1950] += 1
        return cnt.index(max(cnt)) + 1950
