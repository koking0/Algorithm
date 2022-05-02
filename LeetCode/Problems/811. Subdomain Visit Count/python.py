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
