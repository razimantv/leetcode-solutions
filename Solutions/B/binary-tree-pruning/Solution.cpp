// https://leetcode.com/problems/binary-tree-pruning

class Solution {
 public:
  TreeNode* pruneTree(TreeNode* root) {
    if (!root) return root;
    root->left = pruneTree(root->left);
    root->right = pruneTree(root->right);
    return (root->left or root->right or root->val) ? root : nullptr;
  }
};
