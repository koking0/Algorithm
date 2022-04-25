from typing import List


class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        count = 0
        for index in range(3):
            if guess[index] == answer[index]:
                count += 1
        return count
