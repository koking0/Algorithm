class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = maxN = 0
        n, cnt = len(s), [0] * 26

        while right < n:
            cnt[ord(s[right]) - ord("A")] += 1
            maxN = max(maxN, cnt[ord(s[right]) - ord("A")])
            if right - left + 1 - maxN > k:
                cnt[ord(s[left]) - ord("A")] -= 1
                left += 1
            right += 1

        return right - left
