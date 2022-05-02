#include <stack>
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
	int middle_order_traversal(TreeNode* node) {
		if (!node) {
			return 0;
		}
		int pre = -1, ans = INT_MAX;
		stack<TreeNode*> sta;
		TreeNode* item = node;
		while (!sta.empty() || item != nullptr) {
			if (item != nullptr) {
				sta.push(item);
				item = item->left;
			} else {
				item = sta.top();
				if (pre == -1) {
					pre = item->val;
				} else {
					ans = min(ans, item->val - pre);
					pre = item->val;
				}
				sta.pop();
				item = item->right;
			}
		}
		return ans; 
	} 
	
    int getMinimumDifference(TreeNode* root) {
		return middle_order_traversal(root);
    }
};
