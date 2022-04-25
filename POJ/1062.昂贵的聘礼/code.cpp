#include <queue>
#include <iostream>

using namespace std;

int m, n, total = 0;
int graph[107][107], l[107], head[10007], dist[10007];

struct edge {
	int start, end, weight, next;
}edges[10007];

void dijkstra(int start) {
	priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > que;
	for(int i = 1; i <= n; ++i) dist[i] = 2147483647;
	
	dist[start] = 0;
	que.push(make_pair(0, start));
	while(!que.empty()) {
		int now = que.top().second;
		que.pop();
		for(int i=head[now]; i; i = edges[i].next) {
			if(dist[now] + edges[i].weight < dist[edges[i].end]) {
				dist[edges[i].end] = dist[now] + edges[i].weight;
				que.push(make_pair(dist[edges[i].end], edges[i].end));
			}
		}
	}
}

void build(int start, int end, int weight) {
	edges[++total].next = head[start];
	head[start] = total;
	
	edges[total].start = start;
	edges[total].end = end;
	edges[total].weight = weight;
}

int main() {
	int p, x, t, v;
	cin >> m >> n;
	for(int i = 1; i <= n; ++i) {
		cin >> p >> l[i] >> x;
		graph[0][i] = p;
		for(int j = 0; j < x; ++j) {
			cin >> t >> v;
			graph[t][i] = v;
		}
	}
	
	l[0] = l[1];
	for(int i = 0; i <= n; ++i) {
		for(int j = 0; j <= n; ++j) {
			if(abs(l[i] - l[1]) <= m && abs(l[j] - l[1]) <= m && graph[i][j]) {
				build(i, j, graph[i][j]);
			}
		}
	}
	
	dijkstra(0);
	cout << dist[1] << endl;
	return 0;
}
