class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
		long long maxi = 1, res = 0, i = 0;
		while (maxi <= n) {
			if (i < nums.size() && nums[i] < maxi + 1) {
				// ȷ�ϲ�����������Ը��ǵķ�Χ 
				maxi += nums[i++];
			} else {
				// �޷������������ֹ������󸲸Ƿ�Χ��̰�ļ��� maxi �����Ƿ�Χ����һ�� 
				maxi += maxi;
				++res;
			}
		}
		return res;
    }
};
