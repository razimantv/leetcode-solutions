# Find duplicate subtrees

[Problem link](https://leetcode.com/problems/find-duplicate-subtrees/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-duplicate-subtrees/

class Solution {
 public:
  map<vector<int>, pair<int, int>> cnt;
  vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
    int next = 201;
    vector<TreeNode*> ret;
    function<int(TreeNode*)> work = [&](TreeNode* node) {
      if (!node) return 0;
      vector<int> vec{node->val, work(node->left), work(node->right)};
      if (!cnt.count(vec))
        cnt[vec] = {next++, 0};
      else if (!cnt[vec].second++)
        ret.push_back(node);
      return cnt[vec].first;
    };

    work(root);
    return ret;
  }
};
```
## Tags

* [Tree](/README.md#Tree) > [Hashing](/README.md#Tree-Hashing)
* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
* [Dynamic programming](/README.md#Dynamic_programming) > [Trees](/README.md#Dynamic_programming-Trees)
