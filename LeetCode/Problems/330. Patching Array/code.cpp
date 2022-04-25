class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
		long long maxi = 1, res = 0, i = 0;
		while (maxi <= n) {
			if (i < nums.size() && nums[i] < maxi + 1) {
				// 确认并更新数组可以覆盖的范围 
				maxi += nums[i++];
			} else {
				// 无法根据现有数字构建更大覆盖范围则贪心加入 maxi 将覆盖范围扩大一倍 
				maxi += maxi;
				++res;
			}
		}
		return res;
    }
};
