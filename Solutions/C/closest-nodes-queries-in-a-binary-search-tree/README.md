# Closest nodes queries in a binary search tree

[Problem link](https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

class Solution {
 public:
  void work(TreeNode* n, set<int>& s) {
    s.insert(n->val);
    if (n->left) work(n->left, s);
    if (n->right) work(n->right, s);
  }
  vector<vector<int>> closestNodes(TreeNode* root, vector<int>& queries) {
    set<int> s;
    work(root, s);
    int q = queries.size();
    vector<int> qs(q);
    iota(qs.begin(), qs.end(), 0);
    sort(qs.begin(), qs.end(),
         [&](int a, int b) { return queries[a] < queries[b]; });

    auto sit = s.begin();
    vector<vector<int>> ret(q);
    for (int q : qs) {
      int x = queries[q];
      auto& cur{ret[q]};
      while (sit != s.end() and *sit < x) ++sit;
      auto sit2 = sit;
      if (sit != s.begin()) --sit2;
      if (sit != s.end() and *sit == x)
        cur = {x, x};
      else if (sit == s.begin())
        cur = {-1, *sit};
      else if (sit == s.end())
        cur = {*sit2, -1};
      else
        cur = {*sit2, *sit};
    }
    return ret;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Remembering index](/Collections/sorting.md#remembering-index)
