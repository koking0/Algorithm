[268. 丢失的数字](https://leetcode-cn.com/problems/missing-number/)

## Ideas

先排序，排完序之后如果不缺失数字的话，索引和值应该是相等的，所以我们只需要找到第一个索引和值不相等的元素就可以了，说明缺失的是索引代表的值。

如果找到最后发现都没有对不上的，那说明缺失的是最后一个值。

## Code

### C++

```cpp
class Solution {
public:
    int missingNumber(vector<int>& nums) {
		sort(nums.begin(), nums.end());
		for (int i = 0; i < nums.size(); i++) {
			if (i != nums[i]) {
				return i;
			}
		}
		return nums.size();
    }
};
```

### Python

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, v in enumerate(nums):
            if i != v:
                return i
        return len(nums)
```