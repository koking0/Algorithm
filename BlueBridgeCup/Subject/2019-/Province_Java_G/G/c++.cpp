#include <iostream>
#include <algorithm>

using namespace std;

const int maxn = 1e5+7;
int n, m;
int robot_list[maxn];

bool check(int x) {
	int total = 0;
	for (int i = 0; i < m; i++) {
		if (robot_list[i] - x < total + 1) {
			if (robot_list[i] < total + 1) {
				total = robot_list[i] + x - 1;
			} else {
				total += x;
			}
		} else {
			return false;
		}
	}
	return total > n - 1;
}

int main() {
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		cin >> robot_list[i];
	}
	sort(robot_list, robot_list + m);	
	
	int left = 0, right = n, middle, ans;
	while (left < right + 1) {
		middle = (right + left) >> 1;
		if (check(middle)) {
			right = middle - 1;
			ans = middle;
		} else {
			left = middle + 1;
		}
	}
	cout << (ans - 1) * 2 << endl;
	return 0;
}
