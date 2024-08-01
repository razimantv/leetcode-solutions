# Symmetric tree

[Problem link](https://leetcode.com/problems/symmetric-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/symmetric-tree

class Solution {
 public:
  bool work(TreeNode* n1, TreeNode* n2) {
    if (!n1 and !n2) return true;
    return n1 and n2 and (n1->val == n2->val) and work(n1->left, n2->right) and
           work(n1->right, n2->left);
  }
  bool isSymmetric(TreeNode* root) { return work(root, root); }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
