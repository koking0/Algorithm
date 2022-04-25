from copy import deepcopy
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        left, right = 1, 1
        ans, res, sums = [], [], 0
        while right < target:
            sums += right
            while sums > target:
                sums -= left
                res.pop(0)
                left += 1
            res.append(right)
            right += 1
            if sums == target:  # 如果找到一个符合条件的区间
                ans.append(deepcopy(res))
        return ans
