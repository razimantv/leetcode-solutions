# Binary tree maximum path sum

[Problem link](https://leetcode.com/problems/binary-tree-maximum-path-sum)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/binary-tree-maximum-path-sum

class Solution {
 public:
  pair<int, int> two(TreeNode* root) {
    if (root->left == NULL) swap(root->left, root->right);
    int v = root->val, b1 = v, b2 = v;
    if (root->left == NULL) return {b1, b2};

    auto t1 = two(root->left);
    b1 = max(b1, max(v + t1.second, t1.first));
    b2 = max(b2, v + t1.second);

    if (root->right == NULL) return {b1, b2};
    auto t2 = two(root->right);
    b1 = max(b1, max(v + t2.second, t2.first));
    b2 = max(b2, v + t2.second);

    b1 = max(b1, v + t1.second + t2.second);
    return {b1, b2};
  }
  int maxPathSum(TreeNode* root) { return two(root).first; }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
