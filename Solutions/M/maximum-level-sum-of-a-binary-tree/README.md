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

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Iteration](/Collections/tree.md#iteration)
* [Tree](/Collections/tree.md#tree) > [Level-wise processing](/Collections/tree.md#level-wise-processing)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Breadth first search](/Collections/graph-theory.md#breadth-first-search)
* [ChatGPT](/Collections/chatgpt.md#chatgpt)
