#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> addToArrayForm(vector<int>& A, int K) {
    	int n = A.size();
		for(int i = n - 1; i > -1; i--) {
			A[i] += K % 10;
			K = K / 10 + A[i] / 10;
			A[i] %= 10;
		}
		if(K != 0) {
			while(K) {
				A.insert(A.begin(), K % 10);
				K /= 10;
			}
		}
		return A;
    }
};

int main() {
	Solution solution;
	vector<int> A = {2, 1, 5};
	vector<int> res = solution.addToArrayForm(A, 806);
	for (auto item:res) {
		cout << item << endl;
	}
	return 0;
}
