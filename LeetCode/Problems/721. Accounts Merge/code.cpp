class UnionFindSet{
	private:
		int count = 0;
		map<int, int> father;
	public:
		int size() {
			return this->count;
		}
		void add(int x) {
			if (!this->father.count(x)) {
				this->father[x] = x;
				this->count++;
			}
		}
		int find(int x) {
			if (x != this->father[x]) {
				this->father[x] = this->find(this->father[x]);
			}
			return this->father[x];
		}
		void merge(int x, int y) {
			int rootX = this->find(x);
			int rootY = this->find(y);
			if (rootX != rootY) {
				this->father[rootX] = rootY;
				this->count--;
			}
		}
};

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
    	UnionFindSet ufs;
    	map<string, int> msi;		// <email, id> 
    	int n = accounts.size();
		
		for (int i = 0; i < n; i++) {
			ufs.add(i);
			int m = accounts[i].size();
			for (int j = 1; j < m; j++) {
				string str = accounts[i][j];
				if (msi.find(str) == msi.end()) {
					msi[str] = i;
				} else {
					ufs.merge(i, msi[str]);
				}
			}
		}
		
		vector<vector<string>> res;
		map<int, vector<string>> miv;
		for (auto& [k, v]:msi) {
			miv[ufs.find(v)].emplace_back(k);
		}
		for (auto& [k, v]:miv) {
			sort(v.begin(), v.end());
			vector<string> tmp(1, accounts[k][0]);
			tmp.insert(tmp.end(), v.begin(), v.end());
			res.emplace_back(tmp);
		}
		return res;
    }
};
