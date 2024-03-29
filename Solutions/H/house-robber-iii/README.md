# House robber iii

[Problem link](https://leetcode.com/problems/house-robber-iii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/house-robber-iii

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

* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
* [Dynamic programming](/README.md#Dynamic_programming) > [Trees](/README.md#Dynamic_programming-Trees)
