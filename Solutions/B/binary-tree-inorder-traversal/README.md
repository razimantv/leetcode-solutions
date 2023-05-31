# Binary tree inorder traversal

[Problem link](https://leetcode.com/problems/binary-tree-inorder-traversal)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/binary-tree-inorder-traversal

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
 public:
  vector<int> inorderTraversal(TreeNode* root) {
    if (!root) return {};

    vector<int> ret;
    vector<pair<TreeNode*, int>> stk{{root, 0}};

    while (!stk.empty()) {
      auto [node, status] = stk.back();

      if (status == 0) {
        ++stk.back().second;
        if (node->left) stk.push_back({node->left, 0});
      } else {
        stk.pop_back();
        ret.push_back(node->val);
        if (node->right) stk.push_back({node->right, 0});
      }
    }
    return ret;
  }
};
```
## Tags

* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Iteration](/README.md#Tree-Binary_tree-Iteration)
* [Stack](/README.md#Stack) > [Depth first search](/README.md#Stack-Depth_first_search)
