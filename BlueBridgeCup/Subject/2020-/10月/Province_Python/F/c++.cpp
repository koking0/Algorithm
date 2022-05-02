#include <cmath>
#include <iostream> 

using namespace std;

int main() {
	int n, n1 = 0, n2 = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int tmp;
		cin >> tmp;
		if (tmp > 59) {
			n1++;
		}
		if (tmp > 84) {
			n2++;
		}
	}
	cout << round(100.0 * n1 / n) << "%" << endl;
	cout << round(100.0 * n2 / n) << "%" << endl;
	return 0;
}
