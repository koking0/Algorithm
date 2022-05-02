class UnionFindSet{
	private:
		int setSize = 0;
		unordered_map<int, int> father;
	public:
		int find(int x) {
			int root = x;
			while (this->father[root] != -1) {
				root = this->father[root];
			}
			while (x != root) {
				int original = this->father[x];
				this->father[x] = root;
				x = original;
			}
			return root;
		}
		bool isUnion(int x, int y) {
			return this->find(x) == this->find(y);
		}
		bool merge(int x, int y) {
			int rootX = this->find(x);
			int rootY = this->find(y);
			if (rootX != rootY) {
				father[rootX] = rootY;
				this->setSize--;
				return false;
			}
			return true;
		}
		void add(int x) {
			if (!this->father.count(x)) {
				this->father[x] = -1;
				this->setSize++;
			}
		}
}; 

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
		UnionFindSet unionFindSet;
		for (auto& edge:edges) {
			unionFindSet.add(edge[0]);
			unionFindSet.add(edge[1]);
			if (unionFindSet.merge(edge[0], edge[1])) {
				return {edge[0], edge[1]};
			}
		}
		return {};
    }
};
