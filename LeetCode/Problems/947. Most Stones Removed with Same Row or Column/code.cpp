class UnionFindSet{
	private:
		int setSize = 0;
		unordered_map<int, int> father;
	public:
		void add(int x) {
			if (!this->father.count(x)) {
				this->father[x] = -1;
				this->setSize++;
			}
		}
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
		void merge(int x, int y) {
			int rootX = this->find(x);
			int rootY = this->find(y);
			if (rootX != rootY) {
				this->father[rootX] = rootY;
				this->setSize--;
			}
		}
		int getSize() {
			return this->setSize;
		}
};

class Solution {
public:
    int removeStones(vector<vector<int>>& stones) {
    	UnionFindSet unionFindSet;
		for (int i = 0; i < stones.size(); i++) {
			unionFindSet.add(~stones[i][0]);
			unionFindSet.add(stones[i][1]);
			unionFindSet.merge(~stones[i][0], stones[i][1]);
		}
		return stones.size() - unionFindSet.getSize();
    }
};
