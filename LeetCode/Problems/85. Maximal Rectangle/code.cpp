class Solution {
public:
    int maximalRectangle(vector<vector<char> >& matrix) {
    	int m = 0, ans = 0;
    	// n Ϊ matrix �� rows
		int n = matrix.size();
		if (n > 0) {
			// m Ϊ matrix �� cols 
			m = matrix[0].size();
		}
		
		// heights[i][j] ���� [i, j] �ĸ߶� 
		vector<vector<int> > heights(n + 1, vector<int>(m + 1, 0));
		// dp[i][j][k] ������ [i, j] Ϊ���½ǣ��߶�Ϊ k ������ɵ���� 
		vector<vector<vector<int> > > dp(n + 1, vector<vector<int> >(m + 1, vector<int>(n + 1, 0)));
		
		for (int i = 1; i < n + 1; i++) {
			for (int j = 1; j < m + 1; j++) {
				// ������Ͻ��� '0'�����ܹ���ֻ�� '1' �ľ��� 
				if (matrix[i - 1][j - 1] == '0') {
					continue;
				}
				// �߶�Ϊ��һ�еĸ߶�+1 
				heights[i][j] = heights[i - 1][j] + 1;
				// �� [i, j] Ϊ���½Ǽ��㲻ͬ�߶ȵ���� 
				for (int k = 1; k < heights[i][j] + 1; k++) {
					dp[i][j][k] = dp[i][j - 1][k] + k;
					ans = max(ans, dp[i][j][k]);
				}
			}
		}
		return ans;
    }
};
