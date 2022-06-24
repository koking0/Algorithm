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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* res = new ListNode(-1);
		ListNode* prev = res;
		
		while (list1 != nullptr && list2 != nullptr) {
			if (list1->val < list2->val) {
				prev->next = list1;
				list1 = list1->next;
			} else {
				prev->next = list2;
				list2 = list2->next;
			}
			prev = prev->next;
		}
		
		prev->next = list1 == nullptr ? list2 : list1;
		return res->next;
    }
};
