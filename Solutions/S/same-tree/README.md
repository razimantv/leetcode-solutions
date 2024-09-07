# Same tree

[Problem link](https://leetcode.com/problems/same-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/same-tree

class Solution {
 public:
  bool isSameTree(TreeNode* p, TreeNode* q) {
    if (p == NULL and q == NULL) return true;
    if (p == NULL or q == NULL or p->val != q->val) return false;
    return isSameTree(p->left, q->left) and isSameTree(p->right, q->right);
  }
};
```