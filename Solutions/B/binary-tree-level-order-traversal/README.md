# Binary tree level order traversal

[Problem link](https://leetcode.com/problems/binary-tree-level-order-traversal)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/binary-tree-level-order-traversal

class Solution {
 public:
  vector<vector<int>> ret;
  vector<vector<int>> levelOrder(TreeNode* root, int level = 0) {
    if (!root) return {};
    if (ret.size() == level) ret.push_back({});
    ret[level].push_back(root->val);
    levelOrder(root->left, level + 1);
    levelOrder(root->right, level + 1);

    if (level == 0)
      return ret;
    else
      return {};
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
