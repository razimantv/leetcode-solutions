# Balance a binary search tree

[Problem link](https://leetcode.com/problems/balance-a-binary-search-tree/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/balance-a-binary-search-tree/

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root, ar):
            if not root:
                return
            inorder(root. left, ar)
            ar. append(root. val)
            inorder(root. right, ar)

        ar = []
        inorder(root, ar)

        def balanced(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            return TreeNode(ar[m], balanced(l, m - 1), balanced(m+1, r))

        return balanced(0, len(ar) - 1)
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary search tree](/Collections/tree.md#binary-search-tree) > [Traversal](/Collections/tree.md#traversal)
* [Tree](/Collections/tree.md#tree) > [Order traversal](/Collections/tree.md#order-traversal)
* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
