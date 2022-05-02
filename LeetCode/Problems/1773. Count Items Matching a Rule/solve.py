from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans, idx = 0, {"type": 0, "color": 1, "name": 2}
        for item in items:
            if item[idx[ruleKey]] == ruleValue:
                ans += 1
        return ans
