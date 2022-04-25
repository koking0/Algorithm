from collections import Counter
from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans, n, s = 0, len(arr), [0]
        for num in arr:
            s.append(s[-1] ^ num)

        cnt, total = Counter(), Counter()
        for i in range(n):
            if s[i + 1] in cnt:
                ans += cnt[s[i + 1]] * i - total[s[i + 1]]
            cnt[s[i]] += 1
            total[s[i]] += i
        return ans
