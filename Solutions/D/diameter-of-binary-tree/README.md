# Diameter of binary tree

[Problem link](https://leetcode.com/problems/diameter-of-binary-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/diameter-of-binary-tree

class Solution {
 public:
  pair<int, int> both(TreeNode* root) {
    if (root == NULL) return {0, 0};
    auto l = both(root->left), r = both(root->right);
    return {max(l.first, r.first) + 1,
            max(max(l.second, r.second), l.first + r.first + 1)};
  }
  int diameterOfBinaryTree(TreeNode* root) {
    if (root == NULL) return 0;
    return both(root).second - 1;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Trees](/Collections/dynamic-programming.md#trees)
* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
