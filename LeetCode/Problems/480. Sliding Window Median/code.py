from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def median(data):
            data = sorted(data)
            half = len(data) // 2
            return (data[half] + data[~half]) / 2

        left, right, n, ans = 0, k, len(nums), []
        while right < n + 1:
            ans.append(median(nums[left:right]))
            left += 1
            right += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.medianSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
