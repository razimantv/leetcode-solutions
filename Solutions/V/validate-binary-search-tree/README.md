# Validate binary search tree

[Problem link](https://leetcode.com/problems/validate-binary-search-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/validate-binary-search-tree

class Solution {
 public:
  bool isValidBST(TreeNode* root, TreeNode* l = nullptr,
                  TreeNode* r = nullptr) {
    if (l != nullptr and root->val <= l->val) return false;
    if (r != nullptr and root->val >= r->val) return false;
    if (root->left != nullptr and !isValidBST(root->left, l, root))
      return false;
    if (root->right != nullptr and !isValidBST(root->right, root, r))
      return false;
    return true;
  }
};
```