class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    	stack<int> s;
    	map<int, int> record;
    	for (int i = 0; i < nums2.size(); i++) {
    		while (!s.empty() && nums2[i] > nums2[s.top()]) {
    			record[nums2[s.top()]] = nums2[i];
    			s.pop();
			}
			s.push(i);
		}
		
		vector<int> ans;
		for (int i = 0; i < nums1.size(); i++) {
			auto ret = record.find(nums1[i]);
			if (ret != record.end()) {
				ans.push_back(ret -> second);
			} else {
				ans.push_back(-1);
			}
		}
		return ans;
    }
};
