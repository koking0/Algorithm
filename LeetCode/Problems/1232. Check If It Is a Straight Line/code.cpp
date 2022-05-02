class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
		for (int i = 2; i < coordinates.size(); i++)  {
            int k1 = (coordinates[i - 1][0] - coordinates[i - 2][0]) * (coordinates[i][1] - coordinates[i - 1][1]);
            int k2 = (coordinates[i][0] - coordinates[i - 1][0]) * (coordinates[i - 1][1] - coordinates[i - 2][1]);
            if (k1 != k2) {
            	return false;
			}
		}
		return true;
    }
};
