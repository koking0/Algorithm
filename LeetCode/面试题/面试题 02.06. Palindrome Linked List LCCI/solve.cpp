/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
		vector<int> values;
		while (head) {
			values.push_back(head->val);
			head = head->next;
		}
		for (int i = 0, j = values.size() - 1; i < j; i++, j--) {
			if (values[i] != values[j]) {
				return false;
			}
		}
		return true;
    }
};
