# Smallest subtree with all the deepest nodes

[Problem link](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes

class Solution {
 public:
  pair<int, TreeNode*> work(TreeNode* n) {
    if (n == nullptr) return {0, n};
    auto [l1, l2] = work(n->left);
    auto [r1, r2] = work(n->right);
    if (l1 > r1)
      return {l1 + 1, l2};
    else if (l1 < r1)
      return {r1 + 1, r2};
    else
      return {l1 + 1, n};
  }
  TreeNode* subtreeWithAllDeepest(TreeNode* root) { return work(root).second; }
};
```