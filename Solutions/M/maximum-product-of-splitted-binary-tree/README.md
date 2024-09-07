# Maximum product of splitted binary tree

[Problem link](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-product-of-splitted-binary-tree

class Solution {
 public:
  long long T, R;
  int tot(TreeNode* root) {
    if (!root) return 0;
    return root->val + tot(root->left) + tot(root->right);
  }
  int maxProduct(TreeNode* root, int start = 1) {
    if (start) T = tot(root), R = 0;
    int cur = root->val;
    if (root->left) cur += maxProduct(root->left, 0);
    if (root->right) cur += maxProduct(root->right, 0);
    R = max(R, cur * (T - cur));
    return start ? R % 1'000'000'007 : cur;
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
