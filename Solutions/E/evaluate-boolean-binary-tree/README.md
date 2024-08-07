# Evaluate boolean binary tree

[Problem link](https://leetcode.com/problems/evaluate-boolean-binary-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/evaluate-boolean-binary-tree

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
