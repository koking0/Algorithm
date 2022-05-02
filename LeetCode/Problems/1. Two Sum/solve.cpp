#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
		unordered_map<int, int> hash_table;
		for (int i = 0; i < nums.size(); i++) {
			auto flag = hash_table.find(target - nums[i]);
			if (flag != hash_table.end()) {
				return {flag -> second, i};
			}
			hash_table[nums[i]] = i;		// 注意这行代码的位置，必须在 if 判断完之后执行 
		}
		return {};
    }
};

