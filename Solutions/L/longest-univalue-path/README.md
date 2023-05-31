# Longest univalue path

[Problem link](https://leetcode.com/problems/longest-univalue-path)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-univalue-path

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

* [Dynamic programming](/README.md#Dynamic_programming) > [Trees](/README.md#Dynamic_programming-Trees)
* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
