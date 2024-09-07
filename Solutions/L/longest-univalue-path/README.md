# Longest univalue path

[Problem link](https://leetcode.com/problems/longest-univalue-path)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-univalue-path

class Solution {
 public:
  int best;
  int longestUnivaluePath(TreeNode* root, int start = 1) {
    if (start) best = 0;
    if (!root) return 0;
    int l = 0, r = 0;
    if (root->left) {
      int ll = longestUnivaluePath(root->left, 0);
      if (root->val == root->left->val) l = ll;
    }
    if (root->right) {
      int rr = longestUnivaluePath(root->right, 0);
      if (root->val == root->right->val) r = rr;
    }

    best = max(best, l + r);
    return start ? best : (max(l, r) + 1);
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Trees](/Collections/dynamic-programming.md#trees)
* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
