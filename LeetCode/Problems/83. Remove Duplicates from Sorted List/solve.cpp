class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
    	if (!head) {
    		return head;
		}
		ListNode* item = head;
		while (item->next) {
			if (item->val == item->next->val) {
				item->next = item->next->next;
			} else {
				item = item->next;
			}
		}
		return head;
    }
};
