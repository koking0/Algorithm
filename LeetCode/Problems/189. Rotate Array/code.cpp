class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k %= n;		// k ���ܴ������鳤��������Ҫȡ�� 
        if (!k) {	// ��� k = 0 ���÷�ת 
        	return;
		}
		
		// ��ת�������� 
		for (int i = 0, j = --n, a1; i < j; a1 = nums[i], nums[i++]=nums[j], nums[j--]=a1);
		// �ֱ�תǰ k ���ͺ���� 
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
