# Minimum depth of binary tree

[Problem link](https://leetcode.com/problems/minimum-depth-of-binary-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-depth-of-binary-tree

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
  int minDepth(TreeNode* root) {
    if (root == NULL)
      return 0;
    else if (root->left == NULL and root->right == NULL)
      return 1;
    else if (root->left == NULL)
      return 1 + minDepth(root->right);
    else if (root->right == NULL)
      return 1 + minDepth(root->left);
    else
      return 1 + min(minDepth(root->left), minDepth(root->right));
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
