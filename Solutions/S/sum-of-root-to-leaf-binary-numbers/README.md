# Sum of root to leaf binary numbers

[Problem link](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers

class Solution {
  int tot;

 public:
  int sumRootToLeaf(TreeNode* root, bool start = true, int pref = 0) {
    if (root == NULL) return 0;
    if (start) tot = 0;
    pref = (pref << 1) | root->val;
    if (root->left == NULL and root->right == NULL) return tot += pref;
    if (root->left != NULL) sumRootToLeaf(root->left, false, pref);
    if (root->right != NULL) sumRootToLeaf(root->right, false, pref);
    return tot;
  }
};
```