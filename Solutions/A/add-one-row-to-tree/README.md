# Add one row to tree

[Problem link](https://leetcode.com/problems/add-one-row-to-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/add-one-row-to-tree

class Solution {
 public:
  TreeNode* addOneRow(TreeNode* root, int v, int d, int type = 0) {
    if (d == 1) {
      if (type == 0)
        return new TreeNode(v, root, nullptr);
      else if (type == 1)
        return root = new TreeNode(v, root, nullptr);
      else
        root = new TreeNode(v, nullptr, root);
      return root;
    }
    if (root == nullptr) return nullptr;
    root->left = addOneRow(root->left, v, d - 1, 1);
    root->right = addOneRow(root->right, v, d - 1, 2);
    return root;
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
