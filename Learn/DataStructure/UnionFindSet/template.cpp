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
				int o = this->father[x];
				this->father[x] = root;
				x = o;
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
		bool isUnion(int x, int y) {
			return this->find(x) == this->find(y);
		}
}; 
