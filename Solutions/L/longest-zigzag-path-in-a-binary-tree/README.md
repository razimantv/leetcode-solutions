# Longest zigzag path in a binary tree

[Problem link](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

class Solution {
 public:
  tuple<int, int, int> dfs(TreeNode* root) {
    if (!root) return {-1, -1, -1};
    int best{}, left{}, right{};
    auto [lbest, lleft, lright] = dfs(root->left);
    best = max(best, lbest);
    left = lright + 1;
    auto [rbest, rleft, rright] = dfs(root->right);
    best = max(best, rbest);
    right = rleft + 1;
    best = max(best, max(left, right));
    return {best, left, right};
  }
  int longestZigZag(TreeNode* root) { return get<0>(dfs(root)); }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
