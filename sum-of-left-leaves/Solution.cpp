// https://leetcode.com/problems/sum-of-left-leaves

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
 public:
  int sumOfLeftLeaves(TreeNode* root, bool left = false) {
    if (root == NULL) return 0;
    int ret = 0;
    if (left and root->left == NULL and root->right == NULL) return root->val;
    if (root->left != NULL) ret += sumOfLeftLeaves(root->left, true);
    if (root->right != NULL) ret += sumOfLeftLeaves(root->right, false);
    return ret;
  }
};
