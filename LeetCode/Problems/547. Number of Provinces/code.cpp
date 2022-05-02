class UnionFind{
	public:
		int find(int x) {
			int root = x;
			while (father[root] != -1) {
				root = father[root];
			}
			while (x != root) {
				int originalFather = father[x];
				father[x] = root;
				x = originalFather;
			}
			return root;
		}
		
		bool isUnion(int x, int y) {
			return find(x) == find(y);
		}
		
		void merge(int x, int y) {
			int rootX = find(x);
			int rootY = find(y);
			if (rootX != rootY) {
				father[rootX] = rootY;
				setSize--; 
			}
		}
		
		void add(int x) {
			if (!father.count(x)) {
				father[x] = -1;
				setSize++;
			}
		}
		
		int getSetSize() {
			return setSize;
		}
		
		private:
			unordered_map<int, int> father;
			int setSize = 0;
};

class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
		UnionFind uf;
		for(int i = 0; i < isConnected.size(); i++) {
			uf.add(i);
			for (int j = 0; j < i; j++) {
				if (isConnected[i][j]) {
					uf.merge(i, j);
				}
			}
		}
		return uf.getSetSize();
    }
};
