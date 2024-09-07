// https://leetcode.com/problems/construct-string-from-binary-tree

class Solution {
 public:
  string tree2str(TreeNode* root) {
    if (!root) return "";
    string ret = to_string(root->val);
    if (root->left or root->right) ret += "(" + tree2str(root->left) + ")";
    if (root->right) ret += "(" + tree2str(root->right) + ")";
    return ret;
  }
};
