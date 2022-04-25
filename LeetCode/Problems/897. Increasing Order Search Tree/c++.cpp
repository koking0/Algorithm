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
	vector<TreeNode*> middle_order_traversal(TreeNode* node) {
		TreeNode* item = node;
		stack<TreeNode*> stk;
		vector<TreeNode*> ans;
		while (!stk.empty() || item != nullptr) {
			if (item != nullptr) {
				stk.push(item);
				item = item->left;
			} else {
				item = stk.top();
				stk.pop();
				ans.push_back(item);
				item = item->right;
			}
		}
		return ans;
	} 
    TreeNode* increasingBST(TreeNode* root) {
		vector<TreeNode*> values = middle_order_traversal(root);
		for (int i = 0; i < values.size(); i++) {
            if (i == values.size() - 1) {
                values[i]->left = nullptr;
                values[i]->right = nullptr;
            } else {
                cout << values[i]->val << ", ";
                values[i]->left = nullptr;
                values[i]->right = values[i + 1];
            }
		}
		return values[0];
    }
};
