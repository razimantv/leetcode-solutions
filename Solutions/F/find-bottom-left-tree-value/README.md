# Find bottom left tree value

[Problem link](https://leetcode.com/problems/find-bottom-left-tree-value/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-bottom-left-tree-value/

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ret, maxl = root.val, 0

        def work(node, level):
            nonlocal ret, maxl
            if level > maxl:
                ret, maxl = node.val, level
            for child in [node. left, node. right]:
                if child:
                    work(child, level+1)
        work(root, 0)
        return ret
```
## Tags

* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
