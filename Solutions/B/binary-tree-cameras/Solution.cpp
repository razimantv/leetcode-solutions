// https://leetcode.com/problems/binary-tree-cameras

class Solution {
 public:
  // Number in subtree, satisfied, has
  tuple<int, bool, bool> work(TreeNode* root) {
    tuple<int, bool, bool> ret;
    auto& [cnt, sat, has] = ret;
    if (root->left) {
      auto [cc, cs, ch] = work(root->left);
      cnt += cc;
      if (!cs and !has) ++cnt, has = sat = true;
      if (ch) sat = true;
    }
    if (root->right) {
      auto [cc, cs, ch] = work(root->right);
      cnt += cc;
      if (!cs and !has) ++cnt, has = sat = true;
      if (ch) sat = true;
    }

    return {cnt, sat, has};
  }
  int minCameraCover(TreeNode* root) {
    auto [cnt, sat, has] = work(root);
    if (!sat) ++cnt;
    return cnt;
  }
};
