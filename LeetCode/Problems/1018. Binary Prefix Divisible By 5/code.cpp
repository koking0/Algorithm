class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& A) {
    	int pre = 0;
    	vector<bool> res;
    	for (int i = 0; i < A.size(); i++) {
    		pre = ((pre << 1) + A[i]) % 10;
    		res.emplace_back(pre % 5 == 0);
		}
		return res;
    }
};
