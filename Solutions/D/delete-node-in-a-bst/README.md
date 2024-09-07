# Delete node in a bst

[Problem link](https://leetcode.com/problems/delete-node-in-a-bst)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/delete-node-in-a-bst

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

* [Tree](/Collections/tree.md#tree) > [Binary search tree](/Collections/tree.md#binary-search-tree) > [Traversal](/Collections/tree.md#traversal)
* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
