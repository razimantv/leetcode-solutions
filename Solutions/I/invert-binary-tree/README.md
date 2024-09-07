# Invert binary tree

[Problem link](https://leetcode.com/problems/invert-binary-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/invert-binary-tree

class Solution {
 public:
  TreeNode* invertTree(TreeNode* root) {
    if (root == NULL) return root;
    invertTree(root->left);
    invertTree(root->right);
    swap(root->left, root->right);
    return root;
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
