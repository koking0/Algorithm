from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ''
        counter = Counter(list(s))
        for k, v in counter.most_common():
            ans += k * v
        return ans


if __name__ == '__main__':
    print(Solution().frequencySort(s="tree"))
