from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        currentSum = 0
        minn = max(gas)
        for i in range(len(gas)):
            remain = gas[i] - cost[i]
            currentSum += remain

            if currentSum < minn:
                minn = currentSum

        if currentSum < 0:
            return -1
        elif minn > -1:
            return 0

        for i in range(len(gas) - 1, -1, -1):
            remain = gas[i] - cost[i]
            minn += remain
            if minn > -1:
                return i

        return -1


if __name__ == '__main__':
    s = Solution()
    ans = s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
    print(ans)
