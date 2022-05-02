#include <iostream>

using namespace std;

int main() {
	int n, m, end, weight, graph[107][107];
	while(cin >> n && n!= 0) {
       for(int i = 1; i <= n; i ++)
           for(int j = 1; j <= n; j ++)
               graph[i][j] = 999;
		
		for(int i = 1; i < n + 1; i++) {
			cin >> m;
			while(m--) {
				cin >> end >> weight;
				graph[i][end] = weight;
			}
		}
		
		for(int k = 1; k < n + 1; k++) {
			for(int i = 1; i < n + 1; i++) {
				for(int j = 1; j < n + 1; j++) {
					if(i != j && j!= k && i != k && graph[i][j] > graph[i][k] + graph[k][j]) {
						graph[i][j] = graph[i][k] + graph[k][j];
					}
				}
			}
		}
		
		int index, time = 999;
		for(int i = 1; i < n + 1; i++) {
			int sum = 0;
			for(int j = 1; j < n + 1; j++) {
				if(i != j && graph[i][j] > sum) {
					sum = graph[i][j];
				}
			}
			if(sum < time) {
				time = sum;
				index = i;
			}
		}
		cout << index << " " << time << endl;
	}
	return 0;
}
