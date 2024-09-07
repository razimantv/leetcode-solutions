# Construct binary tree from preorder and inorder traversal

[Problem link](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

class Solution {
 public:
  TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder, int l1,
                      int r1, int l2, int r2) {
    TreeNode* ret = new TreeNode(preorder[l1]);
    int i = l2;
    while (inorder[i] != preorder[l1]) ++i;
    if (i != l2)
      ret->left = buildTree(preorder, inorder, l1 + 1, i + l1 - l2, l2, i - 1);
    if (i != r2)
      ret->right = buildTree(preorder, inorder, r1 - r2 + i + 1, r1, i + 1, r2);
    return ret;
  }

  TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
    return buildTree(preorder, inorder, 0, preorder.size() - 1, 0,
                     inorder.size() - 1);
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Order traversal](/Collections/tree.md#order-traversal)
* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
