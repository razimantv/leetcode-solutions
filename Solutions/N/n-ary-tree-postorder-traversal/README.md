# N ary tree postorder traversal

[Problem link](https://leetcode.com/problems/n-ary-tree-postorder-traversal/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def work(node, order):
            if not node:
                return
            for child in node.children:
                work(child, order)
            order.append(node.val)
            return order
        return work(root, [])
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Order traversal](/Collections/tree.md#order-traversal)
* [Tree](/Collections/tree.md#tree) > [N-ary tree](/Collections/tree.md#n-ary-tree)
