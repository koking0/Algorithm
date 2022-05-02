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
	int get_height(TreeNode* node) {
		return node == NULL ? 0 : max(get_height(node->left), get_height(node->right)) + 1;
	}
	
    bool isBalanced(TreeNode* root) {
		return root == NULL ? true : abs(get_height(root->left) - get_height(root->right)) < 2 && isBalanced(root->left) && isBalanced(root->right) ? true : false;
    }
};
