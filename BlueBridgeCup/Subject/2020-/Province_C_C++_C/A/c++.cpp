#include <set>
#include <iostream>

using namespace std;

int main() {
	int n = 78120;
	set<int> s;
	for(int i = 1; i < n + 1; i++) {
		float div = n / i;
		if(i * int(div) == n) {	// 判断 div 是否为整数且满足条件 
			cout << i << " * " << div << " = " << i * div << endl;
			s.insert(i);
			s.insert(int(div));
		}
	}
	cout << "ans = " << s.size() << endl;
	return 0;
}
