# Cousins in binary tree ii

[Problem link](https://leetcode.com/problems/cousins-in-binary-tree-ii/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/cousins-in-binary-tree-ii/

class Solution {
 public:
  vector<int> dsum;
  void dfs(TreeNode* node, int depth) {
    if (!node) return;
    if (depth == dsum.size()) dsum.push_back(0);
    dsum[depth] += node->val;
    dfs(node->left, depth + 1);
    dfs(node->right, depth + 1);
  }

  void dfs2(TreeNode* node, int depth, int sub) {
    if (!node) return;
    node->val = dsum[depth] - sub;
    sub = 0;
    vector<TreeNode*> children{node->left, node->right};
    for (auto child : children)
      if (child) sub += child->val;
    for (auto child : children) dfs2(child, depth + 1, sub);
  }
  TreeNode* replaceValueInTree(TreeNode* root) {
    dfs(root, 0);
    dfs2(root, 0, root->val);
    return root;
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Trees](/Collections/dynamic-programming.md#trees)
