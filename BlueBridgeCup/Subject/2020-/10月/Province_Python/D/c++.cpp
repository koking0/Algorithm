#include <iostream> 

using namespace std;

int main() {
	int n = 20, ans = 1;
	for (int i = 1; i < n; i++) {
		ans += i * 4;
	}
	cout << ans << endl;
	return 0;
}
