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
### Solution.py
```py
# https://leetcode.com/problems/leaf-similar-trees/

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(root):
            if not root:
                return []
            children = leaves(root.left) + leaves(root.right)
            return children if children else [root.val]

        return leaves(root1) == leaves(root2)
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
