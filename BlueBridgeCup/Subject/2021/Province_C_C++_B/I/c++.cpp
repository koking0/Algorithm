#include <iostream>

using namespace std;

const int N = 100010;
pair<int, int> stk[N];
int ans[N];

int main() {
	int n, m, top = 0;
	cin >> n >> m;
	while (m--) {
		int p, q;
		cin >> p >> q;
		if (p == 0) {
			while (top && stk[top].first == 0) {
				q = max(q, stk[top--].second);
			}
			while (top >= 2 && stk[top - 1].second <= q) {
				// 如果当前操作比上一次相同操作的范围要大，那此次操作的前两次操作都将被无效化 
				top -= 2;
			}
			stk[++top] = {0, q};
		} else if (top) {
			while (top && stk[top].first == 1) {
				q = min(q, stk[top--].second);
			}
			while (top >= 2 && stk[top - 1].second >= q) {
				// 如果当前操作比上一次相同操作的范围要大，那此次操作的前两次操作都将被无效化 
				top -= 2;
			}
			stk[++top] = {1, q};
		}
	}
	int left = 1, right = n, k = n;
	for (int i = 1; i < top + 1; i++) {
		if (stk[i].first == 0) {
			while (right > stk[i].second && left < right + 1) {
				ans[right--] = k--;
			}
		} else {
			while (left < stk[i].second && left < right + 1) {
				ans[left++] = k--;
			}
		}
		if (left > right) {
			break;
		}
	}
	if (top % 2) {
		while (left < right + 1) {
			ans[left++] = k--;
		}
	} else {
		while (left < right + 1) {
			ans[right--] = k--;
		}
	}
	for (int i = 1; i < n + 1; i++) {
		cout << ans[i] << " ";
	}
	return 0;
}
