#include <iostream>
#include <cstring>
#include <string>

using namespace std;

char map[11][11]=
					{
						{' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '},
						{' ','U','D','D','L','U','U','L','R','U','L'},
						{' ','U','U','R','L','L','L','R','R','R','U'},
						{' ','R','R','U','U','R','L','D','L','R','D'},
						{' ','R','U','D','D','D','D','U','U','U','U'},
						{' ','U','R','U','D','L','L','R','R','U','U'},
						{' ','D','U','R','L','R','L','D','L','R','L'},
						{' ','U','L','L','U','R','L','L','R','D','U'},
						{' ','R','D','L','U','L','L','R','D','D','D'},
						{' ','U','U','D','D','U','D','U','D','L','L'},
						{' ','U','L','R','D','L','U','U','R','R','R'}
					};
	int people[11][11],ans=0;

bool dfs(int i,int j) {
	if(i > 10 || j > 10 || i < 1 || j < 1) return true;
	if(people[i][j] == 1) return false;

	people[i][j] = 1;
	switch(map[i][j]) {
		case 'U':return dfs(i - 1, j);
		case 'D':return dfs(i + 1, j);
		case 'R':return dfs(i, j + 1);
		case 'L':return dfs(i, j - 1);
		default: return false;
	}
}

int main() {
 	for(int i = 1; i <= 10; i++) {
		for(int j = 1; j <= 10; j++) {
			memset(people, 0, sizeof(people));
			if(dfs(i, j)) ans++;
		}
	}
	cout << ans << endl;
	return 0;
}
