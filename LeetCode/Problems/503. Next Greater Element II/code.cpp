class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
    	stack<int> s;
    	int n = nums.size();
    	vector<int> res(n, -1);
    	for (int i = 0; i < 2 * n; i++) {
    		while (!s.empty() && nums[s.top()] < nums[i % n]) {
    			res[s.top()] = nums[i % n];
    			s.pop();
			}
			s.push(i % n);
		}
		return res;
    }
};
