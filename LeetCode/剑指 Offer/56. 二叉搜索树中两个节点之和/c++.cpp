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
	vector<int> preorder_traversal(TreeNode* node) {
		vector<int> ans;
		stack<TreeNode*> stk;
		stk.push(node);
		while (!stk.empty()) {
			TreeNode* item = stk.top();
			stk.pop();
			ans.push_back(item->val);
			if (item->right != nullptr) {
				stk.push(item->right);
			}
			if (item->left != nullptr) {
				stk.push(item->left);
			}
		}
		return ans;
	}
    bool findTarget(TreeNode* root, int k) {
		if (!root) {
			return false;
		}
		vector<int> preorder_list = preorder_traversal(root);
		
		unordered_map<int, int> hash_table;
		for (int i = 0; i < preorder_list.size(); i++) {
			auto flag = hash_table.find(k - preorder_list[i]);
			if (flag != hash_table.end()) {
				return true;
			}
			hash_table[preorder_list[i]] = i;
		}
		return false;
    }
};
