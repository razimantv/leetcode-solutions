# Binary tree right side view

[Problem link](https://leetcode.com/problems/binary-tree-right-side-view)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/binary-tree-right-side-view

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
  vector<int> tree;
  vector<int> rightSideView(TreeNode* root, int level = 0) {
    if (root == nullptr) return {};

    if (tree.size() <= level)
      tree.push_back(root->val);
    else
      tree[level] = root->val;
    rightSideView(root->left, level + 1);
    rightSideView(root->right, level + 1);

    return level ? vector<int>() : tree;
  }
};
```
## Tags

* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
