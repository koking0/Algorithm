#include <list>
#include <queue>
#include <iostream>
#include <algorithm>

using  namespace std;

class Graph {
	int V;					// ������� 
	int* inDegree;			// �������
	list<int> *adj;			// �ڽӱ� 
	
	int* visit;						// ��������ʱDFS��Ƕ����Ƿ���ʹ� 
	
	public:
		bool haveLoop = false;	// �ж��Ƿ��л� 
		vector<int> topological_seq;	// �������� 
		
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
			BFS Kahn�㷨������̰�ģ�ÿ�δ����Ϊ0�ĵ㿪ʼ������Ϊ�������� 
		*/
		vector <int>().swap(this->topological_seq);	// ����������� 
		
		queue<int> que;		// ���Ϊ0���㼯�� 
		
		// ��ͼ��ѡ�����Ϊ0�ĵ� 
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
			����������ÿ�α�֤��ǰ�����Ϊ0��ű���������Ϊ�������� 
			�������˲��Ƽ�DFS������Ƕ���ͼ����DFS 
			// visit 0 - no visit; 1 - in progress; 2 - visit
		*/
		vector <int>().swap(this->topological_seq);	// ����������� 
		
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
			if (this->visit[u] == 0) {		// δ�������������� 
				dfs(u);
				if (this->haveLoop) return;
			} else if (this->visit[u] == 2) {	// ���������˳� 
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
