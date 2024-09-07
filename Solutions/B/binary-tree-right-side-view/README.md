# Binary tree right side view

[Problem link](https://leetcode.com/problems/binary-tree-right-side-view)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/binary-tree-right-side-view

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

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
