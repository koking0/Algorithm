class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max0, max1 = 0, 0
        cnt, prev = 0, '#'
        for ch in s:
            if ch == prev:
                cnt += 1
            else:
                if prev == '0':
                    max0 = max(max0, cnt)
                elif prev == '1':
                    max1 = max(max1, cnt)
                cnt = 1
            prev = ch
        if prev == '0':
            max0 = max(max0, cnt)
        elif prev == '1':
            max1 = max(max1, cnt)
        return max1 > max0
