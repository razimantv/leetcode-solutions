# Vertical order traversal of a binary tree

[Problem link](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree

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
  map<int, multiset<pair<int, int>>> levels;
  vector<vector<int>> verticalTraversal(TreeNode* root, int depth = 0,
                                        int l = 0) {
    if (root == NULL) return {};
    if (!depth) levels.clear();
    levels[l].insert({depth, root->val});
    if (root->left != NULL) verticalTraversal(root->left, depth + 1, l - 1);
    if (root->right != NULL) verticalTraversal(root->right, depth + 1, l + 1);

    if (!depth) {
      vector<vector<int>> ret;
      for (auto& p : levels) {
        ret.push_back({});
        for (auto v : p.second) ret.back().push_back(v.second);
      }
      return ret;
    }
    return {};
  }
};
```