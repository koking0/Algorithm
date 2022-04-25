#include <string>

class Solution {
public:
    int getDecimalValue(ListNode* head) {
		string str = "";
		while (head) {
			str += to_string(head->val);
			head = head->next;
		}
		cout << str << endl;
		return stoi(str, nullptr, 2);
    }
};
