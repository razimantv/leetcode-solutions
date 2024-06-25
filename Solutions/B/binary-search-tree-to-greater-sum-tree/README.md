# Binary search tree to greater sum tree

[Problem link](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def work(root, add):
            if not root:
                return add
            add = work(root.right, add)
            root.val += add
            add = root.val
            return work(root.left, add)

        work(root, 0)
        return root
```
## Tags

* [Tree](/README.md#Tree) > [Binary search tree](/README.md#Tree-Binary_search_tree)
* [Tree](/README.md#Tree) > [Binary tree](/README.md#Tree-Binary_tree) > [Recursion](/README.md#Tree-Binary_tree-Recursion)
