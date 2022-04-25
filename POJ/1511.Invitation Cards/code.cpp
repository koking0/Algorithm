#include <set>
#include <queue>
#include <cstdio>
#include <cstring>
#include <iostream>

#define INF 0x3f3f3f3f

using namespace std;

const int N = 1e6 + 7;

int p, q, total;
int head[N], rhead[N], dists[N];

struct edge {
	int start, end, weight, next;
}edges[2 * N];

void spfa(int start, int h[]) {
	queue<pair<int, int> > que;
	memset(dists, INF, sizeof(dists));
	
	dists[start] = 0;
	que.push(make_pair(0, start));
	while(!que.empty()) {
		int dist = que.front().first, vertex = que.front().second;
		que.pop();
		
		for(int i = h[vertex]; i; i = edges[i].next) {
			edge item = edges[i];
			if(dists[vertex] + item.weight < dists[item.end]) {
				dists[item.end] = dists[vertex] + item.weight;
				que.push(make_pair(dists[item.end], item.end));
			}
		}
	}
}
 
void build(int h[], int s, int e, int w) {
	edges[total].start = s;
	edges[total].end = e;
	edges[total].weight = w;
	edges[total].next = h[s];
	h[s] = total++;
}
 
int main() {
 	int n;
 	scanf("%d", &n);
 	while(n--) {
 		total = 1;
 		scanf("%d %d", &p, &q);
 		memset(head, 0, sizeof(head));
 		memset(rhead, 0, sizeof(rhead));
 		for(int i = 0; i < q; i++) {
 			int start, end, weight;
 			scanf("%d %d %d", &start, &end, &weight);
 			build(head, start, end, weight);
 			build(rhead, end, start, weight);
		}

		long long ans = 0;
		spfa(1, head);		
		for(int i = 1; i < p + 1; i++) ans += dists[i];
		spfa(1, rhead);
		for(int i = 1; i < p + 1; i++) ans += dists[i];
		printf("%lld\n", ans);
	 }
	 return 0;
 }

