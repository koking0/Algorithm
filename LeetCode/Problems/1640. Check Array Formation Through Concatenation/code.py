from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        arrIndex = 0
        while arrIndex < len(arr):
            for piece in pieces:
                if arr[arrIndex] == piece[0] and arr[arrIndex: arrIndex + len(piece)] == piece:
                    arrIndex += len(piece)
                    break
            else:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    ans = s.canFormArray(arr = [1,3,5,7], pieces = [[2,4,6,8]])
    print(ans)
