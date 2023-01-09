// https://leetcode.com/problems/binary-tree-preorder-traversal/

class Solution {
 public:
  vector<int> ret;
  vector<int> preorderTraversal(TreeNode* root, int start = 1) {
    if (!root) return {};
    ret.push_back(root->val);
    preorderTraversal(root->left, 0);
    preorderTraversal(root->right, 0);
    return start ? ret : vector<int>();
  }
};
