# Count good nodes in binary tree

[Problem link](https://leetcode.com/problems/count-good-nodes-in-binary-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-good-nodes-in-binary-tree

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
  int goodNodes(TreeNode* root, int x = -99999) {
    if (!root) return 0;
    int ret = x <= root->val;
    x = max(x, root->val);
    return ret + goodNodes(root->left, x) + goodNodes(root->right, x);
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
