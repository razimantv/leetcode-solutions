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

* [Tree](/Collections/tree.md#tree) > [Order traversal](/Collections/tree.md#order-traversal)
* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
