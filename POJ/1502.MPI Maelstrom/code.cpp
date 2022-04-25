#include <set>
#include <queue>
#include <cstring>
#include <iostream>
#include <algorithm>

#define INF 0x3f3f3f3f

using namespace std;

int n, graph[107][107], dists[107];

void dijkstra(int start) {
	set<int> visit;
	priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > que;
	for(int i = 0; i < 107; i++) dists[i] = INF;
	
	dists[start] = 0;
	que.push(make_pair(0, start));
	while(!que.empty()) {
		int dist = que.top().first, vertex = que.top().second;
		que.pop();
		visit.insert(vertex);
		
		for(int i = 0; i < n; i++) {
			int val = graph[vertex][i];
			if(val != INF && !visit.count(i) && dist + val < dists[i]) {
				dists[i] = dist + val;
				que.push(make_pair(dists[i], i));
			}
		}
	}
}

int main() {
	cin >> n;

	for(int i = 0; i < 107; i++) {
		for(int j = 0; j < 107; j++) {
			graph[i][j] = i == j ? 0 : INF;
		}
	}
	
	for(int i = 1; i < n; i++) {
		for(int j  = 0; j < i; j++) {
			string str;
			cin >> str;
			if(str == "x") {
				graph[i][j] = INF;
			} else {
				int tmp = 0;
				for(int k = 0; k < str.length(); k++) {
					tmp = tmp * 10 + str[k] - '0';
				}
				graph[i][j] = tmp;
				graph[j][i] = tmp;
			}
		}
	}
	
	dijkstra(0);
	cout << *max_element(dists, dists + n) << endl;
	return 0;
}
