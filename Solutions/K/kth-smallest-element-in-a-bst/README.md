# Kth smallest element in a bst

[Problem link](https://leetcode.com/problems/kth-smallest-element-in-a-bst)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/kth-smallest-element-in-a-bst

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
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

* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
* [Tree](/README.md#Tree) > [Binary search tree](/README.md#Tree-Binary_search_tree)
