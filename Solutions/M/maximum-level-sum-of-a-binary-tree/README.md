# Maximum level sum of a binary tree

[Problem link](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

class Solution {
 public:
  // ChatGPT solution
  int maxLevelSum(TreeNode* root) {
    if (root == nullptr) return 0;

    int maxSum = INT_MIN;
    int maxLevel = 0;
    int level = 0;

    std::queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
      level++;
      int size = q.size();
      int levelSum = 0;

      for (int i = 0; i < size; i++) {
        TreeNode* node = q.front();
        q.pop();

        levelSum += node->val;

        if (node->left) q.push(node->left);

        if (node->right) q.push(node->right);
      }

      if (levelSum > maxSum) {
        maxSum = levelSum;
        maxLevel = level;
      }
    }

    return maxLevel;
  }
};
```
## Tags

* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Iteration](/README.md#Tree-Binary_tree-Iteration)
* [Tree](/README.md#Tree) > [Level-wise processing](/README.md#Tree-Level_wise_processing)
* [Graph theory](/README.md#Graph_theory) > [Breadth first search](/README.md#Graph_theory-Breadth_first_search)
* [ChatGPT](/README.md#ChatGPT)
