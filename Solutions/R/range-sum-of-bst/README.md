# Range sum of bst

[Problem link](https://leetcode.com/problems/range-sum-of-bst)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/range-sum-of-bst

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
  int rangeSumBST(TreeNode* n, int l, int r) {
    if (n == nullptr or l > r) return 0;
    return ((n->val >= l and n->val <= r) ? n->val : 0) +
           rangeSumBST(n->left, l, min(r, n->val)) +
           rangeSumBST(n->right, max(l, n->val), r);
  }
};
```
## Tags

* [Tree](/README.md#Tree) > [Binary search tree](/README.md#Tree-Binary_search_tree)
* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
