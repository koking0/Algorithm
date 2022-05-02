class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        for ch in set(s):
            if s.count(ch) < k:
                return max(self.longestSubstring(t, k) for t in s.split(ch))
        return len(s)


if __name__ == '__main__':
    print(Solution().longestSubstring(s="aaabb", k=3))
