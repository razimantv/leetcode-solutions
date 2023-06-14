// https://leetcode.com/problems/minimum-absolute-difference-in-bst/

class Solution {
 public:
  const int inf = 1'000'000;
  tuple<int, int, int> recurse(TreeNode* root) {
    int best = inf, small = root->val, big = small;
    if (root->left) {
      auto [lbest, lsmall, lbig] = recurse(root->left);
      small = lsmall;
      best = min(best, min(lbest, root->val - lbig));
    }
    if (root->right) {
      auto [rbest, rsmall, rbig] = recurse(root->right);
      big = rbig;
      best = min(best, min(rbest, rsmall - root->val));
    }
    return {best, small, big};
  }
  int getMinimumDifference(TreeNode* root) { return get<0>(recurse(root)); }
};
