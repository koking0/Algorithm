class UnionFindSet {
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
			return this->father[x] == x ? x : this->father[x] = this->find(this->father[x]);
		}
		void merge(int x, int y) {
			int rootX = this->find(x);
			int rootY = this->find(y);
			if (rootX != rootY) {
				this->father[rootX] = rootY;
				this->count--;
			}
		}
		bool isSet(int x, int y) {
			return this->find(x) == this->find(y);
		}
};

class TarjanSCC {
	private:
		int n, ts;
		vector<int> low;
		vector<int> dfn;
		vector<int> ans;
		const vector<vector<int>>& edges;
		const vector<vector<int>>& edgesId;
		
		void getCuttingEdge_(int u, int parentEdgeId) {
			this->low[u] = this->dfn[u] = ++this->ts;
			for (int i = 0; i < this->edges[u].size(); i++) {
				int v = this->edges[u][i];
				int id = this->edgesId[u][i];
				if (this->dfn[v] == -1) {
					this->getCuttingEdge_(v, id);
					this->low[u] = min(this->low[u], this->low[v]);
					if (this->low[v] > this->dfn[u]) {
						this->ans.push_back(id);
					}
				} else if (id != parentEdgeId) {
					this->low[u] = min(this->low[u], this->dfn[v]);
				}
			}
		}
	public:
		TarjanSCC(int n_, const vector<vector<int>>& edges_, const vector<vector<int>>& edgesId_): edges(edges_), edgesId(edgesId_), low(n_, -1), dfn(n_, -1), n(n_), ts(-1) {}
		
		vector<int> getCuttingEdge() {
			for (int i = 0; i < n; i++) {
				if (this->dfn[i] == -1) {
					this->getCuttingEdge_(i, -1);
				}
			}
			return ans;
		}
};

class Solution {
public:
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>>& edges) {
		int m =  edges.size();
		for (int i = 0; i < m; i++) {
			edges[i].push_back(i);
		}
		sort(edges.begin(), edges.end(), [](const auto& u, const auto& v) {
			return u[2] < v[2];
		});
		
		UnionFindSet ufs;
		vector<int> label(m);
		vector<vector<int>> ans(2);
		
		for (int i = 0; i < n; i++) {
			ufs.add(i);
		}
		
		int i = 0;
		while(i < m) {
			int j = i;
			int w = edges[i][2];
			while(j < m && edges[j][2] == edges[i][2]) {
				++j;
			}
			
			int gn = 0;
			map<int, int> compToId;
			
			for (int k = i; k < j; k++) {
				int x = ufs.find(edges[k][0]);
				int y = ufs.find(edges[k][1]);
				if (x != y) {
					if (!compToId.count(x)) {
						compToId[x] = gn++;
					}
					if (!compToId.count(y)) {
						compToId[y] = gn++;
					}
				} else {
					label[edges[k][3]] = -1;
				}
			}
            vector<vector<int>> gm(gn), gmid(gn);
            
            for (int k = i; k < j; ++k) {
                int x = ufs.find(edges[k][0]);
                int y = ufs.find(edges[k][1]);
                if (x != y) {
                    int idx = compToId[x], idy = compToId[y];
                    gm[idx].push_back(idy);
                    gmid[idx].push_back(edges[k][3]);
                    gm[idy].push_back(idx);
                    gmid[idy].push_back(edges[k][3]);
                }
            }

            vector<int> bridges = TarjanSCC(gn, gm, gmid).getCuttingEdge();
            for (int id: bridges) {
                ans[0].push_back(id);
                label[id] = 1;
            }

            for (int k = i; k < j; ++k) {
                ufs.merge(edges[k][0], edges[k][1]);
            }

            i = j;
		}
		
		for (int i = 0; i < m; ++i) {
            if (!label[i]) {
                ans[1].push_back(i);
            }
        }

        return ans;
    }
};
