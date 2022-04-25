class Solution {
public:
    int maximalRectangle(vector<vector<char> >& matrix) {
    	int m = 0, ans = 0;
    	// n 为 matrix 的 rows
		int n = matrix.size();
		if (n > 0) {
			// m 为 matrix 的 cols 
			m = matrix[0].size();
		}
		
		// heights[i][j] 代表 [i, j] 的高度 
		vector<vector<int> > heights(n + 1, vector<int>(m + 1, 0));
		// dp[i][j][k] 代表以 [i, j] 为右下角，高度为 k 可以组成的面积 
		vector<vector<vector<int> > > dp(n + 1, vector<vector<int> >(m + 1, vector<int>(n + 1, 0)));
		
		for (int i = 1; i < n + 1; i++) {
			for (int j = 1; j < m + 1; j++) {
				// 如果左上角是 '0'，则不能构成只含 '1' 的矩形 
				if (matrix[i - 1][j - 1] == '0') {
					continue;
				}
				// 高度为上一行的高度+1 
				heights[i][j] = heights[i - 1][j] + 1;
				// 以 [i, j] 为右下角计算不同高度的面积 
				for (int k = 1; k < heights[i][j] + 1; k++) {
					dp[i][j][k] = dp[i][j - 1][k] + k;
					ans = max(ans, dp[i][j][k]);
				}
			}
		}
		return ans;
    }
};
