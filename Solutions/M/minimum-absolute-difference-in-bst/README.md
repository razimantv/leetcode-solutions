# Minimum absolute difference in bst

[Problem link](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

## Solutions


### Solution.cpp
```cpp
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
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
* [Tree](/Collections/tree.md#tree) > [Binary search tree](/Collections/tree.md#binary-search-tree)
