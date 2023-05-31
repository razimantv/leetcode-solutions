# Binary tree tilt

[Problem link](https://leetcode.com/problems/binary-tree-tilt)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/binary-tree-tilt

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
  pair<int, int> sumtilt(TreeNode* n) {
    if (n == nullptr) return {0, 0};
    auto [s1, t1] = sumtilt(n->left);
    auto [s2, t2] = sumtilt(n->right);
    return {s1 + s2 + n->val, t1 + t2 + abs(s1 - s2)};
  }
  int findTilt(TreeNode* root) { return sumtilt(root).second; }
};
```
## Tags

* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
