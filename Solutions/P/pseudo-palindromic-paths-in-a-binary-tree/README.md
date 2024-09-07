# Pseudo palindromic paths in a binary tree

[Problem link](https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree

class Solution {
 public:
  int pseudoPalindromicPaths(TreeNode* root, int pref = 0) {
    if (root == nullptr)
      return 0;
    else {
      pref ^= 1 << root->val;
      if (root->left == nullptr and root->right == nullptr)
        return ((!pref) or !(pref & (pref - 1)));
      else
        return pseudoPalindromicPaths(root->left, pref) +
               pseudoPalindromicPaths(root->right, pref);
    }
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation) > [Self-inverse property of xor](/Collections/bitwise-operation.md#self-inverse-property-of-xor)
