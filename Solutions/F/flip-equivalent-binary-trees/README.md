# Flip equivalent binary trees

[Problem link](https://leetcode.com/problems/flip-equivalent-binary-trees/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/flip-equivalent-binary-trees/

class Solution:
    def flipEquiv(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        def vec(root):
            if not root: 
                return [-1]
            lc, rc = vec(root.left), vec(root.right)
            return [root.val] + sorted([lc, rc])
        return vec(root1) == vec(root2)
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
* [Flattening](/Collections/flattening.md#flattening)
