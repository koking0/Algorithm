#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	string str;
	while (getline(cin, str)) {
		replace(str.begin(), str.end(), "you", "we");
		cout << str << endl;
	}
	return 0;
}
