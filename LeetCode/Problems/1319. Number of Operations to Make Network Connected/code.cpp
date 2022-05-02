class UnionFindSet {
	private:
		int n, l = 0;
		map<int, int> father;
	public:
		UnionFindSet(int n) {
			this->n = n;
			for(int i = 0; i < n; i++) {
				this->father[i] = i;
			}
		}
		int size() {
			return this->n;
		}
		int less() {
			return this->l;
		}
		int find(int x) {
			return x == this->father[x] ? x : this->father[x] = this->find(this->father[x]);
		}
		void merge(int x, int y) {
			int rootX = this->find(x);
			int rootY = this->find(y);
			if (rootX != rootY) {
				this->father[rootX] = rootY;
				this->n--;
			} else {
				this->l++;
			}
		}
}; 


class Solution {
public:
    int makeConnected(int n, vector<vector<int>>& connections) {
		UnionFindSet ufs(n);
		for(int i = 0; i < connections.size(); i++) {
			ufs.merge(connections[i][0], connections[i][1]);
		}
		int num = ufs.size() - 1;
		return num < ufs.less() + 1 ? num : -1;
    }
};
