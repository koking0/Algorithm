from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        array = [item for item in cnt.items()]
        array.sort(key=lambda x: (-x[1], x[0]))
        return [item[0] for item in array[:k]]


if __name__ == '__main__':
    print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k=2))
