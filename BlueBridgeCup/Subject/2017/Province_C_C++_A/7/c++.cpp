#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;
char s[100];
int len,pos;

int f() {
	int m = 0, tmp = 0;
	while(pos<len) {
		switch(s[pos]) {
			case '(': {
					pos++;
					tmp += f();
					break;
				}
			case ')': {
					pos++;
					m = max(m, tmp);
					return m;
				}
			case 'x': {
					pos++;
					tmp++;
					break;
				}
			case '|': {
					pos++;
					m = max(m, tmp);
					tmp = 0;
					break;
				}
		}
	}
	m = max(m, tmp);
	return m;
}

int main() {
	cin >> s;
	len = strlen(s);
	int ans = f();
	cout << ans << endl;
	return 0;
}
