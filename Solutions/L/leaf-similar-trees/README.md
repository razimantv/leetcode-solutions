# Leaf similar trees

[Problem link](https://leetcode.com/problems/leaf-similar-trees/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/leaf-similar-trees/

class Solution {
 public:
  void work(TreeNode* n, vector<int>& vec) {
    if (n->left) work(n->left, vec);
    if (n->right) work(n->right, vec);
    if (!(n->left) and !(n->right)) vec.push_back(n->val);
  }
  bool leafSimilar(TreeNode* root1, TreeNode* root2) {
    vector<int> v1, v2;
    work(root1, v1);
    work(root2, v2);
    return v1 == v2;
  }
};
```
## Tags

* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
