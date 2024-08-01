# Binary tree level order traversal ii

[Problem link](https://leetcode.com/problems/binary-tree-level-order-traversal-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/binary-tree-level-order-traversal-ii

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
  vector<vector<int>> levelOrderBottom(TreeNode* root) {
    if (root == NULL) return {};
    auto L = levelOrderBottom(root->left), R = levelOrderBottom(root->right);
    vector<vector<int>> ret(max(L.size(), R.size()));
    for (int i = 0; i < ret.size(); i++) {
      if (i < L.size()) ret[ret.size() - i - 1] = L[L.size() - i - 1];
      if (i < R.size()) {
        for (auto r : R[R.size() - i - 1]) ret[ret.size() - i - 1].push_back(r);
      }
    }
    ret.push_back({root->val});
    return ret;
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
