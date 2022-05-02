#include <cstring>
#include <iostream>

using namespace std;

bool mark[4][4];

int main() {
	memset(mark, 0, sizeof(mark));
	for(int i = 0; i < 4; i++) {
		for(int j = 0; j < 4; j++) {
			char ch;
			cin >> ch;
			if(ch == '+') {
				mark[i][j] = !mark[i][j];
				for(int k = 0; k < 4; k++) {
                    mark[i][k] = !mark[i][k];
                    mark[k][j] = !mark[k][j];
                }
			}
		}
	}
	
	int step = 0;
	int p_i[16], p_j[16];
	for(int i = 0; i < 4; i++) {
		for(int j = 0; j < 4; j++) {
			if(mark[i][j]) {
				p_i[step] = i + 1;
				p_j[step] = j + 1;
				step++;
			}
		}
	}
	
	cout << step << endl;
	for(int i = 0; i < step; i++) {
		cout << p_i[i] << " " << p_j[i] << endl;
	}
	return 0;
} 
