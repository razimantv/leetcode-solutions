# Maximum product of splitted binary tree

[Problem link](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-product-of-splitted-binary-tree

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
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

* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
