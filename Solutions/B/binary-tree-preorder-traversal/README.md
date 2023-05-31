# Binary tree preorder traversal

[Problem link](https://leetcode.com/problems/binary-tree-preorder-traversal/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/binary-tree-preorder-traversal/

class Solution {
 public:
  vector<int> ret;
  vector<int> preorderTraversal(TreeNode* root, int start = 1) {
    if (!root) return {};
    ret.push_back(root->val);
    preorderTraversal(root->left, 0);
    preorderTraversal(root->right, 0);
    return start ? ret : vector<int>();
  }
};
```
## Tags

* [Tree](/README.md#Tree) > [Order traversal](/README.md#Tree-Order_traversal)
* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
