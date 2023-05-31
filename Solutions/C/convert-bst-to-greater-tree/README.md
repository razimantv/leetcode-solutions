# Convert bst to greater tree

[Problem link](https://leetcode.com/problems/convert-bst-to-greater-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/convert-bst-to-greater-tree

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
  int pref;
  TreeNode* convertBST(TreeNode* root, int start = 1) {
    if (root == nullptr) return nullptr;
    if (start == 1) pref = 0;
    convertBST(root->right, 0);
    root->val += pref;
    pref = root->val;
    convertBST(root->left, 0);
    return root;
  }
};
```
## Tags

* [Tree](/README.md#Tree) > [Binary search tree](/README.md#Tree-Binary_search_tree) > [Traversal](/README.md#Tree-Binary_search_tree-Traversal)
* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
