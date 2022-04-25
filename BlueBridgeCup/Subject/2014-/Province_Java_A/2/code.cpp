#include <iostream>

using namespace std;

class Solution{
	public:
		void solution() {
			int flag = 1, ans = 0;
			for(int i = 0; i < 100; i++) {
				ans += 4 * flag * (1 / (2 * i + 1));
				flag *= -1;
			}
			cout << ans << endl;
		}
};

int main() {
	Solution solution;
	solution.solution();
	return 0;
}
