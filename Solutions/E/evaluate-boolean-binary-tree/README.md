# Evaluate boolean binary tree

[Problem link](https://leetcode.com/problems/evaluate-boolean-binary-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/evaluate-boolean-binary-tree

class Solution {
 public:
  bool evaluateTree(TreeNode* root) {
    if (!root->left)
      return root->val;
    else if (root->val == 2)
      return evaluateTree(root->left) or evaluateTree(root->right);
    else
      return evaluateTree(root->left) and evaluateTree(root->right);
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
