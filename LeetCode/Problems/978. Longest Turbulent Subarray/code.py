from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left, right, res, n = 0, 0, 1, len(arr)
        while right < n - 1:
            if left == right:
                if arr[left] == arr[left + 1]:
                    left += 1
                right += 1
            else:
                if arr[right - 1] < arr[right] > arr[right + 1]:
                    right += 1
                elif arr[right - 1] > arr[right] < arr[right + 1]:
                    right += 1
                else:
                    left = right
            res = max(res, right - left + 1)
        return res
