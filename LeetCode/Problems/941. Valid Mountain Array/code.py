from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False

        upEndIndex = 0
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                upEndIndex = i
            else:
                break
        if upEndIndex == 0 or upEndIndex == len(A) - 1:
            return False

        for i in range(upEndIndex + 1, len(A)):
            if A[i] >= A[i - 1]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    ans = s.validMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(ans)
