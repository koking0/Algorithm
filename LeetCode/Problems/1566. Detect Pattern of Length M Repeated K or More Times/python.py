from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for left in range(len(arr) - m * k + 1):
            offset = 0
            while offset < m * k:
                if arr[left + offset] != arr[left + offset % m]:
                    break
                offset += 1
            if offset == m * k:
                return True
        return False
