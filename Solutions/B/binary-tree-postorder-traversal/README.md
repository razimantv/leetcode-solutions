# Binary tree postorder traversal

[Problem link](https://leetcode.com/problems/binary-tree-postorder-traversal/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/binary-tree-postorder-traversal/

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def work(node, order):
            if not node:
                return
            for child in [node.left, node.right]:
                work(child, order)
            order.append(node.val)
        order = []
        work(root, order)
        return order
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Order traversal](/Collections/tree.md#order-traversal)
* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
