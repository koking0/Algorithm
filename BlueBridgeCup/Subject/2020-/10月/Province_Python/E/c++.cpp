#include <iostream> 

using namespace std;

int bubble_sort_cnt(char arr[], int n) {
	int cnt = 0;
	for(int i = n - 1; i > -1; i--) {
		for(int j = 0; j < i; j++) {
			if(arr[j] > arr[j + 1]) {
				cnt++;
				swap(arr[j], arr[j + 1]);
			}
		}
	}
	return cnt;
}

int main() {
	int n = 15;
	char a[n] = {'j', 'o', 'n', 'm', 'l', 'k', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'};
	
	cout << bubble_sort_cnt(a, n);
}
