// https://leetcode.com/problems/binary-tree-inorder-traversal


class Solution {
 public:
  vector<int> inorderTraversal(TreeNode* root) {
    if (!root) return {};

    vector<int> ret;
    vector<pair<TreeNode*, int>> stk{{root, 0}};

    while (!stk.empty()) {
      auto [node, status] = stk.back();

      if (status == 0) {
        ++stk.back().second;
        if (node->left) stk.push_back({node->left, 0});
      } else {
        stk.pop_back();
        ret.push_back(node->val);
        if (node->right) stk.push_back({node->right, 0});
      }
    }
    return ret;
  }
};
