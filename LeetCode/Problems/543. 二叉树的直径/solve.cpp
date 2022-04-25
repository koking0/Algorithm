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
	int ans = 1;
	
	int depth(TreeNode* rt) {
		if (rt == NULL) {
			return 0;
		}
		int l_depth = depth(rt->left);
		int r_depth = depth(rt->right);
		ans = max(ans, l_depth + r_depth + 1);
		return max(l_depth, r_depth) + 1;
	} 
public:
    int diameterOfBinaryTree(TreeNode* root) {
		depth(root);
		return ans - 1;
    }
};
