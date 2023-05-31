# Increasing order search tree

[Problem link](https://leetcode.com/problems/increasing-order-search-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/increasing-order-search-tree

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
  TreeNode* increasingBST(TreeNode* root, TreeNode* p = nullptr) {
    if (root == nullptr) return root;
    auto ret = (root->left == nullptr) ? root : increasingBST(root->left, root);
    root->left = nullptr;
    root->right = (root->right == nullptr) ? p : increasingBST(root->right, p);
    return ret;
  }
};
```
## Tags

* [Tree](/README.md#Tree) > [Binary search tree](/README.md#Tree-Binary_search_tree) > [Traversal](/README.md#Tree-Binary_search_tree-Traversal)
* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
