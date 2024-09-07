# Kth smallest element in a bst

[Problem link](https://leetcode.com/problems/kth-smallest-element-in-a-bst)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/kth-smallest-element-in-a-bst

class Solution {
 public:
  pair<int, int> work(TreeNode* root, int k) {
    if (root == NULL) return {0, 0};
    auto l = work(root->left, k);
    if (l.first) return l;
    if (l.second == k - 1) return {1, root->val};
    auto r = work(root->right, k - 1 - l.second);
    if (r.first) return r;
    return {0, l.second + r.second + 1};
  }
  int kthSmallest(TreeNode* root, int k) { return work(root, k).second; }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
* [Tree](/Collections/tree.md#tree) > [Binary search tree](/Collections/tree.md#binary-search-tree)
