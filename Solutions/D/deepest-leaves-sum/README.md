# Deepest leaves sum

[Problem link](https://leetcode.com/problems/deepest-leaves-sum)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/deepest-leaves-sum

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
  int depth, tot;
  int deepestLeavesSum(TreeNode* root, int d = 0) {
    if (root == nullptr) return 0;
    if (!d) depth = tot = 0;
    if (root->left == nullptr and root->right == nullptr) {
      if (d > depth)
        depth = d, tot = root->val;
      else if (d == depth)
        tot += root->val;
    }
    deepestLeavesSum(root->left, d + 1);
    deepestLeavesSum(root->right, d + 1);
    return tot;
  }
};
```
## Tags

* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
