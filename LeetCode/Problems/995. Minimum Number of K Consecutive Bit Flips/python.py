from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n, ans, total = len(nums), 0, 0
        diff = [0] * (n + 1)
        for i in range(n):
            total += diff[i]
            if (total & 1) ^ nums[i] == 0:
                if i + k > n:
                    return -1
                diff[i] += 1
                if i + k < n:
                    diff[i + k] -= 1
                total += 1
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minKBitFlips(nums=[0, 0, 0, 1, 0, 1, 1, 0], k=3))
