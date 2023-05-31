# Distribute coins in binary tree

[Problem link](https://leetcode.com/problems/distribute-coins-in-binary-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/distribute-coins-in-binary-tree

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

* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
