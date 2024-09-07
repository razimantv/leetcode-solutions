// https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree

class Solution {
 public:
  int pseudoPalindromicPaths(TreeNode* root, int pref = 0) {
    if (root == nullptr)
      return 0;
    else {
      pref ^= 1 << root->val;
      if (root->left == nullptr and root->right == nullptr)
        return ((!pref) or !(pref & (pref - 1)));
      else
        return pseudoPalindromicPaths(root->left, pref) +
               pseudoPalindromicPaths(root->right, pref);
    }
  }
};
