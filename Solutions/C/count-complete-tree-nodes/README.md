# Count complete tree nodes

[Problem link](https://leetcode.com/problems/count-complete-tree-nodes)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-complete-tree-nodes

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
  int countNodes(TreeNode* root) {
    int ret = 0;
    queue<TreeNode*> bfsq;
    if (root != NULL) bfsq.push(root);
    while (!bfsq.empty()) {
      TreeNode* cur = bfsq.front();
      bfsq.pop();

      ret++;
      if (cur->left != NULL) bfsq.push(cur->left);
      if (cur->right != NULL) bfsq.push(cur->right);
    }
    return ret;
  }
};
```
## Tags

* [Fraud](/README.md#Fraud)
