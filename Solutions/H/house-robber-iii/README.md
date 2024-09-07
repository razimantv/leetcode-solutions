# House robber iii

[Problem link](https://leetcode.com/problems/house-robber-iii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/house-robber-iii

class Solution {
 public:
  pair<int, int> work(TreeNode* root) {
    int y = root->val, n = 0;
    if (root->left) {
      auto [ly, ln] = work(root->left);
      y += ln;
      n += ly;
    }
    if (root->right) {
      auto [ry, rn] = work(root->right);
      y += rn;
      n += ry;
    }
    return {max(y, n), n};
  }
  int rob(TreeNode* root) { return root ? work(root).first : 0; }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Trees](/Collections/dynamic-programming.md#trees)
