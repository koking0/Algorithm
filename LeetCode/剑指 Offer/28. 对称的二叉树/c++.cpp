/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
	bool check(TreeNode* m, TreeNode* n) {
		if (!m && !n) return true;
		if (!m || !n) return false;
		return m->val == n->val && check(m->left, n->right) && check(m->right, n->left);
	}
    bool isSymmetric(TreeNode* root) {
    	return check(root, root);
    }
};
