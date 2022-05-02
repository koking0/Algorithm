[414. 第三大的数](https://leetcode-cn.com/problems/third-maximum-number/)

## Ideas

emmmm，内置排序算法YYDS，三行代码解决。

## Code

### C++

```cpp
class Solution {
public:
    int thirdMax(vector<int>& nums) {
    	set<int> s (nums.begin(), nums.end());
    	nums.assign(s.begin(), s.end());
		sort(nums.begin(), nums.end());
		int n = nums.size();
		return nums[n < 3 ? n - 1 : n - 3];
    }
};
```

### Python

```python
class Solution:
	def thirdMax(self, nums: List[int]) -> int:
		nums = list(set(nums))
		nums.sort()
		return nums[-1 if len(nums) < 3 else -3]
```