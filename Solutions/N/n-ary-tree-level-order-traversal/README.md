# N ary tree level order traversal

[Problem link](https://leetcode.com/problems/n-ary-tree-level-order-traversal)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/n-ary-tree-level-order-traversal


class Solution {
 public:
  vector<vector<int>> levelOrder(Node* root) {
    if (!root) return {};

    vector<vector<int>> ret;
    vector<Node*> cur{root};
    while (!cur.empty()) {
      vector<Node*> next;
      ret.push_back({});
      for (auto n : cur) {
        ret.back().push_back(n->val);
        for (auto nn : n->children) next.push_back(nn);
      }
      cur = next;
    }
    return ret;
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Order traversal](/Collections/tree.md#order-traversal)
