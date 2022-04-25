from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        return list(str(int("".join(list(map(str, A)))) + K))


if __name__ == "__main__":
    solution = Solution()
    print(solution.addToArrayForm([1,2,0,0], 34))
