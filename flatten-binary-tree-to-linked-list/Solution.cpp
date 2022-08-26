// https://leetcode.com/problems/flatten-binary-tree-to-linked-list

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
  TreeNode *work(TreeNode *root) {
    TreeNode *ret = root;
    if (root->left) {
      ret = work(root->left);
      ret->right = root->right;
      root->right = root->left;
      root->left = nullptr;
    }
    if (ret->right) ret = work(ret->right);
    return ret;
  }

  void flatten(TreeNode *root) {
    if (root == nullptr) return;
    work(root);
  }
};
