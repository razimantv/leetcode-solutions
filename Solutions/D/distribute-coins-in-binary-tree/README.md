# Distribute coins in binary tree

[Problem link](https://leetcode.com/problems/distribute-coins-in-binary-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/distribute-coins-in-binary-tree

class Solution {
 public:
  int ret;
  pair<int, int> work(TreeNode* root) {
    if (!root) return {0, 0};

    int n = 1, c = root->val;

    auto [ln, lc] = work(root->left);
    ret += abs(ln - lc);
    n += ln;
    c += lc;

    auto [rn, rc] = work(root->right);
    ret += abs(rn - rc);
    n += rn;
    c += rc;

    return {n, c};
  }
  int distributeCoins(TreeNode* root) {
    ret = 0;
    work(root);
    return ret;
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
