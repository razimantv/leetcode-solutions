// https://leetcode.com/problems/increasing-order-search-tree

class Solution {
 public:
  TreeNode* increasingBST(TreeNode* root, TreeNode* p = nullptr) {
    if (root == nullptr) return root;
    auto ret = (root->left == nullptr) ? root : increasingBST(root->left, root);
    root->left = nullptr;
    root->right = (root->right == nullptr) ? p : increasingBST(root->right, p);
    return ret;
  }
};
