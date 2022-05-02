#include <iostream>

using namespace std;

int gcd(int a, int b) {
	// 辗转相除法求最大公约数
	return b == 0 ? a : gcd(b, a % b); 
}

int main() {
	int ans = 0;
	for(int zi = 1; zi < 2021; zi++) {
		for(int mu = 1; mu < 2021; mu++) {
			if(gcd(zi, mu) == 1) {
				ans++;
			}
		}
	}
	cout << "ans = " << ans << endl;
	return 0;
} 
