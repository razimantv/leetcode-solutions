# Flatten binary tree to linked list

[Problem link](https://leetcode.com/problems/flatten-binary-tree-to-linked-list)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/flatten-binary-tree-to-linked-list

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
  TreeNode *work(TreeNode *root) {
    TreeNode *ret = root;
    if (root->left) {
      ret = work(root->left);
      ret->right = root->right;
      root->right = root->left;
      root->left = nullptr;
    }
    if (ret->right) ret = work(ret->right);
    return ret;
  }

  void flatten(TreeNode *root) {
    if (root == nullptr) return;
    work(root);
  }
};
```
## Tags

* [Linked list](/Collections/linked-list.md#linked-list) > [Iteration](/Collections/linked-list.md#iteration)
* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
* [Flattening](/Collections/flattening.md#flattening)
