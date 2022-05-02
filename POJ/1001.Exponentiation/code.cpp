#include <cstring>
#include <iostream> 

using namespace std;

int n;
string s;

class bigInt{
	public:
		int num[1000], len, base;
	public:
		bigInt() {
			this->base = 10;
			memset(this->num, 0, sizeof(this->num));
		}
		void input(int a) {
			int i = 0;
			if(a == 0) {
				this->len = 1;
			}
			for(i = 0; a; i++) {
				this->num[i] = a % this->base;
				a /= this->base;
			}
			this->len = i;
		}
		bigInt operator *(const bigInt &a) const {
			bigInt ans;
			for(int i = 0; i < len; i++) {
				for(int j = 0; j < a.len; j++) {
					ans.num[i + j] += this->num[i] * a.num[j];
				}
			}
			ans.len = this->len + a.len - 1;
			for(int i = 0; i < ans.len; i++) {
				if(ans.num[i] >= this->base) {
					ans.num[i + 1] += ans.num[i] / this->base;
					ans.num[i] %= this->base;
				}
			}
			if(ans.num[ans.len]) {
				ans.len++;
			}
			return ans;
		}
};

bigInt qpow(bigInt n, int d) {
	bigInt ans;
	ans.input(1);
	while(d) {
		if(d & 1) {
			ans = ans * n;
		}
		n = n * n;
		d >>= 1;
	}
	return ans;
}
	
int main() {
	while(cin >> s >> n) {
		int i, j, num = 0;
		for(i = 0; s[i]; i++) {
			if(s[i] == '.') {
				j = i;
			} else {
				num = num * 10 + s[i] - '0';
			}
		}
		
		int l = (i - j - 1) * n;
		bigInt ans;
		ans.input(num);
		ans = qpow(ans, n);
		for(i = ans.len - 1; i > l - 1; i--){
			cout << ans.num[i];
		}
		
		for(j = 0; ans.num[j] == 0; j++);
		if(i > j) cout << ".";
		
		for(int i = l - 1; i > j - 1; i--){
			cout << ans.num[i];
		}
		cout << endl;
	}
	return 0;
}
