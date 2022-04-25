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
