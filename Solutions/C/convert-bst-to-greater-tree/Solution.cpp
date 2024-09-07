// https://leetcode.com/problems/convert-bst-to-greater-tree

class Solution {
 public:
  int pref;
  TreeNode* convertBST(TreeNode* root, int start = 1) {
    if (root == nullptr) return nullptr;
    if (start == 1) pref = 0;
    convertBST(root->right, 0);
    root->val += pref;
    pref = root->val;
    convertBST(root->left, 0);
    return root;
  }
};
