# Cousins in binary tree

[Problem link](https://leetcode.com/problems/cousins-in-binary-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/cousins-in-binary-tree

class Solution {
 public:
  void work(TreeNode* root, int parent, int depth,
            map<int, pair<int, int>>& pdmap) {
    if (root == NULL) return;
    pdmap[root->val] = {parent, depth};
    work(root->left, root->val, depth + 1, pdmap);
    work(root->right, root->val, depth + 1, pdmap);
  }
  bool isCousins(TreeNode* root, int x, int y) {
    map<int, pair<int, int>> pdmap;
    work(root, -1, 0, pdmap);

    auto pdx = pdmap[x], pdy = pdmap[y];
    return pdx.first != pdy.first and pdx.second == pdy.second;
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
