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
    vector<int> reversePrint(ListNode* head) {
		vector<int> ans;
		while (head) {
			ans.insert(ans.begin(), head->val);
			head = head->next;
		}
		return ans;
    }
};
