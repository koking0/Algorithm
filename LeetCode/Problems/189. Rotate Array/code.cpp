class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k %= n;		// k 可能大于数组长度所以需要取余 
        if (!k) {	// 如果 k = 0 则不用反转 
        	return;
		}
		
		// 反转整个数组 
		for (int i = 0, j = --n, a1; i < j; a1 = nums[i], nums[i++]=nums[j], nums[j--]=a1);
		// 分别反转前 k 个和后面的 
		for (int i = 0, j = k - 1, a1, a2; i < j || k < n;) {
			if (i < j) {
				a1 = nums[i];
				nums[i++] = nums[j];
				nums[j--] = a1;
			}
			if (k < n) {
				a2 = nums[k];
				nums[k++] = nums[n];
				nums[n--] = a2;
			}
		}
    }
};
