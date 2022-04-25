[451. 根据字符出现频率排序](https://leetcode-cn.com/problems/sort-characters-by-frequency/)

## Ideas

Python解法：用个计数器，然后遍历计数器把相应字符乘以出现次数拼接起来就可以了。

## Code

### Python

```python
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
```