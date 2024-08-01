# Construct string from binary tree

[Problem link](https://leetcode.com/problems/construct-string-from-binary-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/construct-string-from-binary-tree

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
  string tree2str(TreeNode* root) {
    if (!root) return "";
    string ret = to_string(root->val);
    if (root->left or root->right) ret += "(" + tree2str(root->left) + ")";
    if (root->right) ret += "(" + tree2str(root->right) + ")";
    return ret;
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
