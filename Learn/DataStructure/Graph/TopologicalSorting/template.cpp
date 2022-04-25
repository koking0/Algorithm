#include <list>
#include <queue>
#include <iostream>
#include <algorithm>

using  namespace std;

class Graph {
	int V;					// 顶点个数 
	int* inDegree;			// 顶点入度
	list<int> *adj;			// 邻接表 
	
	int* visit;						// 拓扑排序时DFS标记顶点是否访问过 
	
	public:
		bool haveLoop = false;	// 判断是否有环 
		vector<int> topological_seq;	// 拓扑序列 
		
	Graph(int v) {
		this->V = v;
		this->adj = new list<int>[v];
		this->inDegree = new int[v];
		this->visit = new int[v];
		for(int i = 0; i < v; i++) {
			this->inDegree[i] = 0;
			this->visit[i] = 0;
		}
	}
	~Graph() {
		delete [] this->adj;
		delete [] this->inDegree;
	}
	void addEdge(int v, int w) {
		this->adj[v].push_back(w);
		this->inDegree[w]++;
	}
	
	void topologicalSort_BFS() {
		/*
			BFS Kahn算法，基于贪心，每次从入度为0的点开始，正序为拓扑序列 
		*/
		vector <int>().swap(this->topological_seq);	// 清空拓扑序列 
		
		queue<int> que;		// 入度为0顶点集合 
		
		// 从图中选择入度为0的点 
		for(int i = 0; i < this->V; i++) {
			if (this->inDegree[i] == 0) {
				que.push(i);
			}
		}
		// BFS 
		while(!que.empty()) {
			int front = que.front();
			que.pop();
			this->topological_seq.push_back(front);
			for(int item:this->adj[front]) {
				if (!(--this->inDegree[item])) {
					que.push(item);
				}
			}
		}
		this->haveLoop = this->topological_seq.size() == this->V ? false : true;
	}
	void topologicalSort_DFS() {
		/*
			基于搜索，每次保证当前点出度为0后才遍历，逆序为拓扑序列 
			单纯拓扑不推荐DFS，如果是二分图才用DFS 
			// visit 0 - no visit; 1 - in progress; 2 - visit
		*/
		vector <int>().swap(this->topological_seq);	// 清空拓扑序列 
		
		for (int i = 0; i < this->V; i++) {
			if (!this->visit[i]) {  
				dfs(i);
				if (this->haveLoop) return;
			}
		}
		reverse(this->topological_seq.begin(), this->topological_seq.end());
	}
	void dfs(int v) {
		for (auto u: this->adj[v]) {
			if (this->visit[u] == 0) {		// 未搜索，继续深入 
				dfs(u);
				if (this->haveLoop) return;
			} else if (this->visit[u] == 2) {	// 遇到环，退出 
				this->haveLoop = true;
				return;
			}
		}
		this->visit[v] = 1;
		this->topological_seq.push_back(v);
	}
	void printTopologicalSeq() {
	    if (!this->haveLoop) {
		    for (int item:this->topological_seq) {
		    	cout << item << " ";
			}
		} else {
			cout << "Graph have loop!";
		}
		cout << endl;
	}
};

int main(){
    Graph graph(8);
    graph.addEdge(0,1);
    graph.addEdge(0,2);
    graph.addEdge(2,4);
    graph.addEdge(1,4);
    graph.addEdge(1,3);
    graph.addEdge(4,3);
    graph.addEdge(4,5);
    graph.addEdge(4,6);
    graph.addEdge(3,5);
    graph.addEdge(6,7);
    graph.addEdge(5,7);
    graph.addEdge(3,7);
    
    graph.topologicalSort_BFS();
	graph.printTopologicalSeq();
	
	graph.topologicalSort_DFS();
	graph.printTopologicalSeq();
    return 0;
}
