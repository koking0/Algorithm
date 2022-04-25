#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main(){
	long long num_10 = 0;
	string str;
	cin >> str;
	
	for(int i = 0; i < str.length(); i++){
		if (str[str.length() - 1 - i] >= 'A' && str[str.length() - 1 - i] <= 'F'){
			num_10 += (str[str.length() - 1 - i] - 55) * pow(16, i);
		}
		if (str[str.length() - 1 - i] >= '1' && str[str.length() - 1 - i] <= '9'){
			num_10 += (str[str.length() - 1 - i] - 48) * pow(16, i);
		}
	}
	cout << num_10 << endl;
	return 0;
}
