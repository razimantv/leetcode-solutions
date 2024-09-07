# Find a corresponding node of a binary tree in a clone of that tree

[Problem link](https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree


class Solution {
 public:
  TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned,
                          TreeNode* target) {
    if (original == nullptr)
      return original;
    else if (original == target)
      return cloned;
    auto ret = getTargetCopy(original->left, cloned->left, target);
    if (ret != nullptr) return ret;
    return getTargetCopy(original->right, cloned->right, target);
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
