// https://leetcode.com/problems/flatten-binary-tree-to-linked-list

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
