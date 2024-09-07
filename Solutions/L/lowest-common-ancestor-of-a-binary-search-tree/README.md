# Lowest common ancestor of a binary search tree

[Problem link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree


class Solution {
 public:
  bool has(TreeNode* root, TreeNode* n) {
    if (!root)
      return false;
    else if (root == n)
      return true;
    else
      return has(root->left, n) or has(root->right, n);
  }
  TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (root == p or root == q) return root;
    bool lp = has(root->left, p), lq = has(root->left, q);
    if (lp != lq)
      return root;
    else if (lp)
      return lowestCommonAncestor(root->left, p, q);
    else
      return lowestCommonAncestor(root->right, p, q);
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
