# Binary tree zigzag level order traversal

[Problem link](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

class Solution {
  vector<vector<int>> ans;

 public:
  vector<vector<int>> zigzagLevelOrder(TreeNode* root, int level = 0) {
    if (root == NULL) return {};
    if (!level) ans.clear();
    if (level == ans.size()) ans.push_back({});
    ans[level].push_back(root->val);
    if (root->left != NULL) zigzagLevelOrder(root->left, level + 1);
    if (root->right != NULL) zigzagLevelOrder(root->right, level + 1);
    if (!level) {
      for (int i = 1; i < ans.size(); i += 2)
        reverse(ans[i].begin(), ans[i].end());
      return ans;
    }
    return {{}};
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
