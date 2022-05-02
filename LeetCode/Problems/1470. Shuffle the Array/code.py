from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        tmp = []
        for i in range(n):
            tmp.append(nums[i])
            tmp.append(nums[n + i])
        return tmp


if __name__ == '__main__':
    s = Solution()
    ans = s.shuffle(nums=[1, 2, 3, 4, 4, 3, 2, 1], n=4)
    print(ans)
