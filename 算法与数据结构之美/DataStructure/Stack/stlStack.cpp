#include <iostream> 
#include <stack>

using namespace std;

int main() {
	stack<int> intStack;
	stack<float> floatStack;
	stack<string> stringStack;
	
	intStack.push(1);
	intStack.push(2);
	intStack.push(3);
	while (!intStack.empty()) {
		cout << intStack.top() << " ";
		intStack.pop();
	}
	cout << endl;
	
	for (int i = 0; i < 7; i++) {
		intStack.push(i);
	}
	cout << "intStack top = " << intStack.top() << endl;
	cout << "intStack size = " << intStack.size() << endl;
	return 0;
}
