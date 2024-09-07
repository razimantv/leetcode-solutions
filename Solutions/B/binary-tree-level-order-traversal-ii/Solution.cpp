// https://leetcode.com/problems/binary-tree-level-order-traversal-ii

class Solution {
 public:
  vector<vector<int>> levelOrderBottom(TreeNode* root) {
    if (root == NULL) return {};
    auto L = levelOrderBottom(root->left), R = levelOrderBottom(root->right);
    vector<vector<int>> ret(max(L.size(), R.size()));
    for (int i = 0; i < ret.size(); i++) {
      if (i < L.size()) ret[ret.size() - i - 1] = L[L.size() - i - 1];
      if (i < R.size()) {
        for (auto r : R[R.size() - i - 1]) ret[ret.size() - i - 1].push_back(r);
      }
    }
    ret.push_back({root->val});
    return ret;
  }
};
