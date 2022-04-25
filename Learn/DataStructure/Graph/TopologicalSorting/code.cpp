#include <list>
#include <queue>
#include <iostream>

using  namespace std;

class Graph {
	int V;				// 顶点个数 
	int* indegree;		// 顶点入度 
	list<int> *adj;		// 邻接表 
	
	public:
	Graph(int v) {
		this->V = v;
		this->adj = new list<int>[v];
		this->indegree = new int[v];
		for(int i = 0; i < v; i++) {
			this->indegree[i] = 0;
		}
	}
	~Graph() {
		delete [] this->adj;
		delete [] this->indegree;
	}
	void addEdge(int v, int w) {
		this->adj[v].push_back(w);
		this->indegree[w]++;
	}
	vector<int> topologicalSort() {
		vector<int> res;
		queue<int> que;
		
		for (int i=0; i < this->V; i++) {
			if (this->indegree[i] == 0) {
				que.push(i);
			}
		}
		while (!que.empty()) {
			int front = que.front();
			que.pop();
			res.push_back(front);
			for (int item:this->adj[front]) {
				if (!(--this->indegree[item])) {
					que.push(item);
				}
			}
		}
		return res.size() == this->V ? res : vector<int> ();
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
    for (int item:graph.topologicalSort()) {
    	cout << item << " ";
	}
    return 0;
}
