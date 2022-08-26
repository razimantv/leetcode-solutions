// https://leetcode.com/problems/sum-root-to-leaf-numbers

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
  int sumNumbers(TreeNode* root, int pref = 0) {
    if (root == NULL) return 0;
    if (root->left == NULL and root->right == NULL)
      return pref * 10 + root->val;
    int ret = 0;
    if (root->right != NULL)
      ret += sumNumbers(root->right, pref * 10 + root->val);
    if (root->left != NULL)
      ret += sumNumbers(root->left, pref * 10 + root->val);
    return ret;
  }
};
