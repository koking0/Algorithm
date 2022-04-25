#include <iostream>
#include <cstring>
#include <string>
#include <cmath>

using namespace std;

int main(){
	long long num_10 = 0;
	string str;
	int n;
	cin >> n;
	while(n--){
		cin >> str;
	
		for(int i = 0; i < str.length(); i++){
			if (str[str.length() - 1 - i] >= 'A' && str[str.length() - 1 - i] <= 'F'){
				num_10 += (str[str.length() - 1 - i] - 55) * pow(16, i);
			}
			if (str[str.length() - 1 - i] >= '1' && str[str.length() - 1 - i] <= '9'){
				num_10 += (str[str.length() - 1 - i] - 48) * pow(16, i);
			}
		}
		
		int i = 0;
		int num_8[256];
		memset(num_8, 0, 256);
		while(num_10 > 0){
			num_8[i++] = num_10 % 8;
			num_10 /= 8;
		}
		int ans = 0;
		for(; i > -1; i--){
			ans += pow(10, i) * num_8[i];
		}
		printf("%d\n", ans);
	}
	return 0;
}
