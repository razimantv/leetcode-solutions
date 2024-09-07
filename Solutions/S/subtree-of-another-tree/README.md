# Subtree of another tree

[Problem link](https://leetcode.com/problems/subtree-of-another-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/subtree-of-another-tree

class Solution {
 public:
  bool isEqual(TreeNode* root, TreeNode* sub) {
    if (!root and !sub) return true;
    if (!root or !sub) return false;
    return root->val == sub->val and isEqual(root->left, sub->left) and
           isEqual(root->right, sub->right);
  }
  bool isSubtree(TreeNode* root, TreeNode* sub) {
    if (!root) return false;
    if (isSubtree(root->left, sub) or isSubtree(root->right, sub)) return true;
    return root->val == sub->val and isEqual(root, sub);
  }
};
```