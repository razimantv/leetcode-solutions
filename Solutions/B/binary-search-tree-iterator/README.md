# Binary search tree iterator

[Problem link](https://leetcode.com/problems/binary-search-tree-iterator)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/binary-search-tree-iterator

class BSTIterator {
 public:
  vector<pair<bool, TreeNode*>> vec;

  BSTIterator(TreeNode* root) {
    if (root == nullptr) return;
    do {
      vec.push_back({true, root});
      root = root->left;
    } while (root != nullptr);
  }

  int next() {
    auto ret = vec.back().second->val;
    vec.back().first = false;

    auto next = vec.back().second->right;
    while (next != nullptr) {
      vec.push_back({true, next});
      next = next->left;
    }

    while (!vec.empty() and !vec.back().first) vec.pop_back();
    return ret;
  }

  bool hasNext() { return !vec.empty(); }
};

```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary search tree](/Collections/tree.md#binary-search-tree) > [Traversal](/Collections/tree.md#traversal)
* [Stack](/Collections/stack.md#stack)
