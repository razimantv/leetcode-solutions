# Recover binary search tree

[Problem link](https://leetcode.com/problems/recover-binary-search-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/recover-binary-search-tree

class Solution {
 public:
  vector<TreeNode*> nodes;

  void findnodes(TreeNode* root) {
    nodes.push_back(root);
    if (root->left != nullptr) findnodes(root->left);
    if (root->right != nullptr) findnodes(root->right);
  }

  bool isbad(TreeNode* root, int l, int r) {
    if (root->val < l or root->val > r) return true;
    return (root->left != nullptr and isbad(root->left, l, root->val)) or
           (root->right != nullptr and isbad(root->right, root->val, r));
  }
  void recoverTree(TreeNode* root) {
    findnodes(root);
    int N = nodes.size();
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < i; ++j) {
        swap(nodes[i]->val, nodes[j]->val);
        if (!isbad(root, INT_MIN, INT_MAX)) return;
        swap(nodes[i]->val, nodes[j]->val);
      }
    }
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
* [Tree](/Collections/tree.md#tree) > [Binary search tree](/Collections/tree.md#binary-search-tree)
