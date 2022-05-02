#include <climits>
#include <iomanip>
#include <iostream>

using namespace std;

int main() {
	int n, max_num = INT_MIN, min_num = INT_MAX, sum = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int num;
		cin >> num;
		max_num = max(max_num, num);
		min_num = min(min_num, num);
		sum += num;
	}
	cout << max_num << endl << min_num << endl << fixed << setprecision(2) << 1.0 * sum / n << endl;
	return 0;
}
