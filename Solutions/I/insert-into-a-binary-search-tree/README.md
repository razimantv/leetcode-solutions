# Insert into a binary search tree

[Problem link](https://leetcode.com/problems/insert-into-a-binary-search-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/insert-into-a-binary-search-tree

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
  TreeNode* insertIntoBST(TreeNode* root, int val) {
    if (root == nullptr) return new TreeNode(val);
    if (val > root->val)
      root->right = insertIntoBST(root->right, val);
    else
      root->left = insertIntoBST(root->left, val);
    return root;
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary search tree](/Collections/tree.md#binary-search-tree)
