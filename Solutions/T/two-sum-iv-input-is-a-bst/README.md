# Two sum iv input is a bst

[Problem link](https://leetcode.com/problems/two-sum-iv-input-is-a-bst)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/two-sum-iv-input-is-a-bst

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
  unordered_set<int> s;
  void work(TreeNode* n) {
    if (!n) return;
    s.insert(n->val);
    work(n->left);
    work(n->right);
  }
  bool findTarget(TreeNode* root, int k) {
    work(root);
    for (int x : s)
      if (2 * x != k and s.count(k - x)) return true;
    return false;
  }
};
```