/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
		ListNode* pre = new ListNode(0, head);
		ListNode* item = pre;
		while (item->next != NULL) {
			if (item->next->val == val) {
				item->next = item->next->next;
			} else {
				item = item->next;
			}
		}
		return pre->next;
    }
};
