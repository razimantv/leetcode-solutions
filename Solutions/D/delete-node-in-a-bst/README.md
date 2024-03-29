# Delete node in a bst

[Problem link](https://leetcode.com/problems/delete-node-in-a-bst)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/delete-node-in-a-bst

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
  TreeNode* deleteNode(TreeNode* root, int key) {
    if (root == NULL) return NULL;
    if (key < root->val) {
      root->left = deleteNode(root->left, key);
      return root;
    }
    if (key > root->val) {
      root->right = deleteNode(root->right, key);
      return root;
    }

    if (root->left == NULL)
      return root->right;
    else if (root->right == NULL)
      return root->left;

    TreeNode* cur = root->left;
    while (cur->right != NULL) cur = cur->right;
    cur->right = root->right;

    return root->left;
  }
};
```
## Tags

* [Tree](/README.md#Tree) > [Binary search tree](/README.md#Tree-Binary_search_tree) > [Traversal](/README.md#Tree-Binary_search_tree-Traversal)
* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
