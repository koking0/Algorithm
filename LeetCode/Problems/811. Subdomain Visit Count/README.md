## Ideas

计数配对域名是由域名访问次数和域名组成的，那么对应域名的每一级域名都访问了相应次。

那么我们可以遍历计数配对域名组成的数组，对于每个计数配对域名，可以先把域名按照`.`分隔开，然后由一个总的计数器累加每一级域名的访问次数。

## Code 

```python
from typing import List
from collections import Counter


class Solution:
	def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
		counter = Counter()
		for cp in cpdomains:
			cnt, domain = cp.split(' ')
			domains = domain.split('.')
			for i, v in enumerate(domains):
				counter['.'.join(domains[i:])] += int(cnt)
		ans = []
		for k, v in counter.items():
			ans.append(f"{v} {k}")
		return ans


if __name__ == '__main__':
	cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
	solution = Solution().subdomainVisits(cpdomains)
	print(solution)
```