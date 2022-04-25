[389. 找不同](https://leetcode-cn.com/problems/find-the-difference/)

## Ideas

emmm，排个序，然后挨个比较？

## Code

### Python

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for i, v in enumerate(s):
            if t[i] != v:
                return t[i]
        return t[-1]
```