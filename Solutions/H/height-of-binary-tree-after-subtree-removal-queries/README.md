# Height of binary tree after subtree removal queries

[Problem link](https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

class Solution {
 public:
  vector<vector<int>> vertices;
  unordered_map<int, pair<int, int>> work;

  void dfs(TreeNode* root, int depth) {
    int val = root->val;
    auto& [d, maxd] = work[val];
    d = depth;
    if (vertices.size() == d) vertices.push_back({});
    vertices[d].push_back(val);

    maxd = d;
    if (root->left) {
      dfs(root->left, depth + 1);
      maxd = max(maxd, work[root->left->val].second);
    }
    if (root->right) {
      dfs(root->right, depth + 1);
      maxd = max(maxd, work[root->right->val].second);
    }
  }
  vector<int> treeQueries(TreeNode* root, vector<int>& queries) {
    dfs(root, 0);

    for (auto& level : vertices) {
      const int L = level.size();
      for (int i = 0; i < min(2, L); ++i) {
        int best = i;
        for (int j = i + 1; j < L; ++j) {
          if (work[level[j]].second > work[level[best]].second) best = j;
        }
        swap(level[best], level[i]);
      }
    }

    for (int& q : queries) {
      int d = work[q].first;
      if (vertices[d].size() == 1)
        q = d - 1;
      else if (vertices[d][0] == q)
        q = work[vertices[d][1]].second;
      else
        q = work[vertices[d][0]].second;
    }
    return queries;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Trees](/Collections/dynamic-programming.md#trees)
* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
* [Tree](/Collections/tree.md#tree) > [Order traversal](/Collections/tree.md#order-traversal)
