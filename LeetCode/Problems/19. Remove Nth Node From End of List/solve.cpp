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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
    	ListNode* pre = new ListNode(0, head);
		ListNode* slow = pre;
		ListNode* quick = head;
		
		for (int i = 0; i < n; i++) {
			quick = quick->next;
		}
		
		while (quick) {
			quick = quick->next;
			slow = slow->next;
		}
		slow->next = slow->next->next;
		return pre->next;
    }
};
