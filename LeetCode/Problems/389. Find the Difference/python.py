class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for i, v in enumerate(s):
            if t[i] != v:
                return t[i]
        return t[-1]
