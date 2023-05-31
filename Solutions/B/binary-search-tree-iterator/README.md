# Binary search tree iterator

[Problem link](https://leetcode.com/problems/binary-search-tree-iterator)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/binary-search-tree-iterator

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

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
```
## Tags

* [Tree](/README.md#Tree) > [Binary search tree](/README.md#Tree-Binary_search_tree) > [Traversal](/README.md#Tree-Binary_search_tree-Traversal)
* [Stack](/README.md#Stack)
