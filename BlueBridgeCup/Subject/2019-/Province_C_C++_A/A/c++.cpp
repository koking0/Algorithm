#include <iostream> 

using namespace std;

bool check(int num) {
	while (num) {
		int item = num % 10;
		if (item == 2 or item == 0 or item == 1 or item == 9) {
			return true;
		}
		num /= 10;
	}
	return false;
}

int main() {
	long long ans1 = 0, ans2 = 0;
	for (int i = 1; i < 2020; i++) {
		if (check(i)) {
			ans1 += i;
			ans2 += i * i;
		}
	}
	cout << ans1 << endl << ans2 << endl;
	return 0;
}
