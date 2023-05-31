# Balanced binary tree

[Problem link](https://leetcode.com/problems/balanced-binary-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/balanced-binary-tree

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
  pair<bool, int> work(TreeNode* root) {
    if (root == nullptr) return {true, 0};
    auto [f1, d1] = work(root->left);
    if (!f1) return {false, -1};
    auto [f2, d2] = work(root->right);
    return {f2 && abs(d1 - d2) < 2, max(d1, d2) + 1};
  }
  bool isBalanced(TreeNode* root) { return work(root).first; }
};
```
## Tags

* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
