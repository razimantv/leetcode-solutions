# Path sum ii

[Problem link](https://leetcode.com/problems/path-sum-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/path-sum-ii

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
  vector<int> cur;
  vector<vector<int>> ret;
  vector<vector<int>> pathSum(TreeNode* root, int targetSum, int start = 1) {
    if (start and !root) return {};
    targetSum -= root->val;
    cur.push_back(root->val);
    if (targetSum == 0 and !root->left and !root->right) ret.push_back(cur);
    if (root->left) pathSum(root->left, targetSum, 0);
    if (root->right) pathSum(root->right, targetSum, 0);
    cur.pop_back();
    if (start)
      return ret;
    else
      return {};
  }
};
```
## Tags

* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
* [Backtracking](/README.md#Backtracking) > [Push and pop for efficient state update](/README.md#Backtracking-Push_and_pop_for_efficient_state_update)
