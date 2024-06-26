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

* [Tree](/README.md#Tree) > [Binary search tree](/README.md#Tree-Binary_search_tree) > [Traversal](/README.md#Tree-Binary_search_tree-Traversal)
* [Tree](/README.md#Tree) > [Order traversal](/README.md#Tree-Order_traversal)
* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
